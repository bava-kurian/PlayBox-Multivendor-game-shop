from django.contrib import admin
from django.urls import path,include
from core.views import BaseView,IndexView
from django.conf import settings
from django.conf.urls.static import static
import store,user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',BaseView.as_view(),name="base"),
    path('',IndexView,name='index'),
    path('',include('store.urls')),
    path('',include('user.urls')),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)