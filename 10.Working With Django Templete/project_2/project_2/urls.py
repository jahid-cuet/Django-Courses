
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('first_app/',include('first_app.urls') ),
]
