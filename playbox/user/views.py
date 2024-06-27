from django.shortcuts import render,redirect,get_object_or_404
from store.models import Product,Category,Cart,CartItem
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from store.froms import ProductForm,VendorForm
from django.utils.text import slugify
from django.contrib import messages
from store.models import Order,OrderItem
# Create your views here.

def VendorDetailView(request,pk):
    user=User.objects.get(pk=pk)
    vendor=UserProfile.objects.get(pk=pk)
    product=Product.objects.filter(user=vendor)
    return render(request,'user/vendor_detail.html',
                  {'vendor':vendor,
                   'product':product,})
    
def SignupView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            userprofile=UserProfile.objects.create(user=user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'user/signup.html', {'form': form})

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})
@login_required
def LogoutConfirmView(request):
    return render(request,'user/logout_confirm.html')
@login_required
def LogoutView(request):
        logout(request)
        return redirect('index')
@login_required
def ProfileView(request):
    user=UserProfile.objects.get(user=request.user)
    products=Product.objects.filter(user=user)
    orders = Order.objects.filter(user=request.user)
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()
    
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    return render(request,'user/user_profile.html',{'products':products,
                                                    'user':user,
                                                    'orders':orders,
                                                    'cart_items':cart_items},)
@login_required
def MyStoreView(request):
    user=UserProfile.objects.get(pk=request.user.pk)
    products=Product.objects.filter(user=user)
    ordres=OrderItem.objects.filter(product__user=user)
    return render(request,'user/my_store.html',{'products':products,
                                                'orders':ordres})

@login_required
def AddProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.user = UserProfile.objects.get(user=request.user)
            product.slug = slugify(product.name)
            product.save()

            messages.success(request, 'The product was added!')

            return redirect('my_store')
    else:
        form = ProductForm()
    categories = Category.objects.all()
    return render(request, 'user/add_product.html', {'form': form, 'categories': categories})
@login_required
def RemoveProduct(request,slug):
    user=UserProfile.objects.get(user=request.user)
    product=Product.objects.get(slug=slug,user=user)
    
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'The product was deleted!')
        return redirect('my_store')
    
    return render(request, 'user/confirm_remove_product.html', {'product': product})
@login_required
def EditProduct(request,slug):
    
    user=UserProfile.objects.get(user=request.user)
    product=Product.objects.get(slug=slug,user=user)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.slug = slugify(product.name)
            product.save()
            messages.success(request,"The product was edited!")
            return redirect('my_store')
    else:
        form = ProductForm(instance=product)
    
    categories = Category.objects.all()
    
    return render(request, 'user/edit_product.html', {'form': form, 
                                                      'categories': categories, 
                                                      'product': product})
            
@login_required
def Become_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.is_vendor = True
            user_profile.save()
            messages.success(request, 'Your profile has been updated successfully and you are now a vendor!')
            return redirect('my_store')
    else:
        form = VendorForm(instance=request.user.userprofile)

    return render(request, 'user/become_vendor.html', {'form': form})