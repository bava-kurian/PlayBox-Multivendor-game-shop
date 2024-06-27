from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,DetailView
from .models import Product,Category,Cart,CartItem,Order,OrderItem
from user.models import UserProfile
from django.db.models import Q
from django.contrib.auth.decorators import login_required
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

@login_required
def Checkout(request):
    cart=Cart.objects.get(user=request.user)
    cart_items = cart.items.all()
    cart_count=0
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    cart_count=sum( item.quantity for item in cart_items)
    form = OrderForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
    
            order = form.save(commit=False)
            order.created_by = request.user
            order.paid_amount = total_price
            order.save()
            for item in cart_items:
                product = item.product
                quantity = int(item.quantity)
                price = product.price * quantity

                item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)
            cart.delete()
            return redirect('index')
        else:
            form = OrderForm()
    return render(request, 'store/checkout.html', {'cart_items': cart_items,
                                                   'total_price':total_price,
                                                   'total_items':cart_count,
                                                   'form':form})
    
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