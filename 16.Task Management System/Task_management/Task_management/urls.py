
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('Add_Task/',include('task.urls')),
    path('Add_Category/',include('category.urls')),
]
