from django.urls import path
from posts.views import Add_Post,edit_Post,delete_Post

urlpatterns = [

    path('add/', Add_Post ,name='add_Post'),
    path('edit/<int:id>',edit_Post ,name='edit_Post'),
    path('delete/<int:id>',delete_Post ,name='delete_Post'),
   
]