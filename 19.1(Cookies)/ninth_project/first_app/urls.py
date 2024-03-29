from django.urls import path,include
from .import views

urlpatterns = [

    path('',views.set_session),
    path('get/',views.get_cook),
    path('del/',views.delete_cookie),
]