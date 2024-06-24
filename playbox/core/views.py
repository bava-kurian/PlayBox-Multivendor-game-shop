from django.shortcuts import render
from django.views.generic import TemplateView,list
from store.models import Product
# Create your views here.

class BaseView(TemplateView):
    template_name="core/base.html"
    

def IndexView(request):
    new_arrivals = Product.objects.all()[:4]
    consoles = Product.objects.filter(category=1)[:4]
    games = Product.objects.filter(category='2')[:4]
    accessories = Product.objects.filter(category='3')[:4]
    
    context = {
        'new_arrivals': new_arrivals,
        'consoles': consoles,
        'games': games,
        'accessories': accessories,
    }
    
    return render(request, 'core/index.html', context)

    