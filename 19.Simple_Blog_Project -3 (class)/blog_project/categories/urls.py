from django.urls import path
from categories.views import Add_Categories

urlpatterns = [

    path('add/', Add_Categories ,name='Add_Categories'),
   
]