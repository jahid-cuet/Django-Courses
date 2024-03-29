
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home' ),
    path('add_musician/',include('musician.urls') ),
    path('add_album/',include('Album.urls') ),
]
