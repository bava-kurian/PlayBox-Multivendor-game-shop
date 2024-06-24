from django.urls import path
from django.conf.urls import static
from django.conf import settings
from . import views

urlpatterns = [
    path("product/<slug:slug>/",views.ProductDetailView,name='product_details'),
    path('categories/',views.CategoryListView,name='categories_list'),
    path('category/<slug:slug>/',views.category_detail,name='category_detail'),
    path('search/',views.Search,name='search'),
]
