import razorpay
from django.conf import settings
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,DetailView
from .models import Product,Category,Cart,CartItem,Order,OrderItem
from user.models import UserProfile
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .froms import OrderForm
# Create your views here.

def ProductDetailView(request,slug):
    product=Product.objects.get(slug=slug)
    category_hierarchy = product.get_category_hierarchy()
    return render(request, 'store/product_detail.html', {'product': product, 
                                                   'category_hierarchy': category_hierarchy})

def CategoryListView(request):
    categories=Category.objects.all()
    return render (request,'store/category_list.html',{'categories':categories})

def get_all_subcategories(category):
    subcategories = category.subcategories.all()
    all_subcategories = list(subcategories)
    for subcategory in subcategories:
        all_subcategories.extend(get_all_subcategories(subcategory))
    return all_subcategories

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    subcategories = get_all_subcategories(category)
    all_categories = [category] + subcategories
    products = Product.objects.filter(category__in=all_categories)
    
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'store/category_detail.html', context)

def Search(request):
    query = request.GET.get('q')
    
    results = Product.objects.filter(Q(name__icontains=query)|Q(description__contains=query))  
    print('query:',results)
    return render(request, 'store/search.html', {'query': query, 'results': results})

@login_required
def AddToCart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')

@login_required
def ViewCart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'store/view_cart.html', {'cart_items': cart_items,'total_price':total_price})

@login_required
def RemoveFormCart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()

    return redirect('view_cart')

@login_required
def IncrementQuantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

@login_required
def DecrementQuantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('view_cart')

# Razorpay client initialization
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET_KEY))
amount=0
@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            for item in cart.items.all():
                OrderItem.objects.create(order=order, product=item.product, price=item.product.price, quantity=item.quantity)
            
            amount = int(cart.get_total_price())* 100
            print(amount)
            razorpay_order = razorpay_client.order.create(dict(amount=amount, currency='INR', payment_capture='0'))
            
            order.payment_intent = razorpay_order['id']
            print("orderid:",order.payment_intent)
            order.paid_amount = amount
            order.save()
            
            context = {
                'order': order,
                'razorpay_key': settings.RAZORPAY_KEY_ID,
                'amount': amount,
                'razorpay_order_id': razorpay_order['id'],
                'callback_url': request.build_absolute_uri('/payment/callback/')
            }
            
            return render(request, 'store/payment.html', context)
    else:
        form = OrderForm()
    
    return render(request, 'store/checkout.html', {'form': form, 'cart': cart})

@csrf_exempt
def payment_callback(request):
    if request.method == 'POST':
        payment_data = request.POST
        razorpay_order_id = payment_data.get('razorpay_order_id')
        razorpay_payment_id = payment_data.get('razorpay_payment_id')
        razorpay_signature = payment_data.get('razorpay_signature')
        
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        }
        
        result = razorpay_client.utility.verify_payment_signature(params_dict)
        if result:
            try:
                order = Order.objects.get(payment_intent=razorpay_order_id)
                amount = int(order.paid_amount)
                print("ammount:",amount)
                razorpay_client.payment.capture(razorpay_payment_id, amount)
                order.is_paid = True
                order.save()
                return redirect('payment_success')
            except Order.DoesNotExist:
                print("order doesnot exist")
                return redirect('payment_failure')
            except Exception as e:
                print("Payment capture error:", e)
                return redirect('payment_failure')
        else:
            return redirect('payment_failure')

    return redirect('payment_failure')

@login_required
def payment_success(request):
    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        cart.delete() 
    return render(request, 'store/payment_success.html')

@login_required
def payment_failure(request):
    return render(request, 'store/payment_failure.html')

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/order_history.html', {'orders': orders})
    
@login_required
def OrderSingle(request,slug):
    product=Product.objects.get(slug=slug)
    form = OrderForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
    
            order = form.save(commit=False)
            order.created_by = request.user
            order.paid_amount = product.price
            order.save()
            return redirect('index')
        else:
            form = OrderForm()
    return render(request, 'store/order_single.html', {'product': product,
                                                   'total_price':product.price,
                                                   'form':form})
    
def OrderDetails(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = OrderItem.objects.filter(order=order)
    
    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'store/order_details.html', context)