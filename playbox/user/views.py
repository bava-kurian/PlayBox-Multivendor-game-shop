from django.shortcuts import render,redirect,get_object_or_404
from store.models import Product,Category
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from store.froms import ProductForm
from django.utils.text import slugify
from django.contrib import messages
# Create your views here.

def VendorDetailView(request,pk):
    user=User.objects.get(pk=pk)
    vendor=UserProfile.objects.get(pk=pk)
    product=Product.objects.filter(user=vendor)
    return render(request,'user/vendor_detail.html',
                  {'vendor':user,'product':product})
    
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
    user=UserProfile.objects.get(pk=request.user.pk)
    products=Product.objects.filter(user=user)
    return render(request,'user/user_profile.html',{'products':products})
@login_required
def MyStoreView(request):
    user=UserProfile.objects.get(pk=request.user.pk)
    products=Product.objects.filter(user=user)
    return render(request,'user/my_store.html',{'products':products})

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
            messages.success(request,"The wproduct was edited!")
            return redirect('my_store')
    else:
        form = ProductForm(instance=product)
    
    categories = Category.objects.all()
    
    return render(request, 'user/edit_product.html', {'form': form, 'categories': categories, 'product': product})
            
            
