from django.urls import path
from profiles.views import Add_Profile

urlpatterns = [

    path('add/', Add_Profile ,name='Add_Profile'),
   
]