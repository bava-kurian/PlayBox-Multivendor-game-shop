from django.shortcuts import render
from django.views.generic import TemplateView,list
from store.models import Product,Category
# Create your views here.

class BaseView(TemplateView):
    template_name="core/base.html"
    

def IndexView(request):
    new_arrivals = Product.objects.all()[:4]
    category1=Category.objects.get(slug='consoles')
    category2=Category.objects.get(slug='controllers')
    category3=Category.objects.get(slug='accessories')
    category4=Category.objects.get(slug='games')
    
    consoles = Product.objects.filter(category=category1.id)[:4]
    controllers = Product.objects.filter(category=category2)[:4]
    accessories = Product.objects.filter(category=category3)[:4]
    games = Product.objects.filter(category=category4)[:4]
    
    context = {
        'new_arrivals': new_arrivals,
        'consoles': consoles,
        'controllers': controllers,
        'accessories': accessories,
        'games':games,
    }
    
    return render(request, 'core/index.html', context)

    
def custom_404(request, exception):
    return render(request, 'user/404.html', status=404)