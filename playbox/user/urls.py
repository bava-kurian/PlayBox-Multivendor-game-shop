from django.urls import path

from . import views

urlpatterns = [
    path('vendor/<int:pk>/',views.VendorDetailView,name='vendor_detail'),
    path('signup/',views.SignupView,name='signup'),
    path('login/',views.LoginView,name='login'),
    path('profile/',views.ProfileView,name='user_profile'),
    path('logout_confirm/',views.LogoutConfirmView,name='logout_confirm'),
    path('logout/',views.LogoutView,name='logout'),
    path('mystore/',views.MyStoreView,name='my_store'),
    path('add_product/',views.AddProduct,name='add_product'),
    path('remove_product/<slug:slug>',views.RemoveProduct,name='remove_product'),
    path('edit_product/<slug:slug>',views.EditProduct,name='edit_product'),
]
