from django.urls import path
from django.conf.urls import static
from django.conf import settings
from . import views

urlpatterns = [ 
    path("product/<slug:slug>/",views.ProductDetailView,name='product_details'),
    path('categories/',views.CategoryListView,name='categories_list'),
    path('category/<slug:slug>/',views.category_detail,name='category_detail'),
    path('search/',views.Search,name='search'),
    path('add_to_cart/<int:product_id>/', views.AddToCart, name='add_to_cart'),
    path('increment_quantity/<int:cart_item_id>/', views.IncrementQuantity, name='increment_quantity'),
    path('decrement_quantity/<int:cart_item_id>/', views.DecrementQuantity, name='decrement_quantity'),
    path('view_cart/', views.ViewCart, name='view_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.RemoveFormCart, name='remove_from_cart'),
    path('checkout/',views.Checkout,name='checkout'),
    path('order_single/<slug:slug>/',views.OrderSingle,name="order_single"),
]