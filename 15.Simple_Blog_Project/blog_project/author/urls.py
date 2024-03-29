from django.urls import path
from author.views import Add_Author

urlpatterns = [

    path('add/',Add_Author,name='Add_Author'),
   
]