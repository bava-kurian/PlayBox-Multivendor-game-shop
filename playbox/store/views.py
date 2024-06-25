from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,DetailView
from .models import Product,Category
from django.db.models import Q
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