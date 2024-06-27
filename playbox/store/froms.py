from django.forms import ModelForm
from django import forms
from .models import Product,Order
from user.models import UserProfile
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'description', 'price', 'image','stock',)
        
class OrderForm(ModelForm):
    class Meta:
        model=Order
        
        fields=('first_name','last_name','address','email','phone','zipcode','city',)
        
class VendorForm(forms.ModelForm):
    accept_terms = forms.BooleanField(required=True, label="I accept the terms and conditions")

    class Meta:
        model = UserProfile
        fields = ['vendor_name', 'address', 'phone', 'email', 'accept_terms']