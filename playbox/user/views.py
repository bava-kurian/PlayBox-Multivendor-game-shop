from django.shortcuts import render,redirect
from store.models import Product
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
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

def LogoutConfirmView(request):
    return render(request,'user/logout_confirm.html')

def LogoutView(request):
        logout(request)
        return redirect('index')

def ProfileView(request):
    user=UserProfile.objects.get(pk=request.user.pk)
    products=Product.objects.filter(user=user)
    return render(request,'user/user_profile.html',{'products':products})
