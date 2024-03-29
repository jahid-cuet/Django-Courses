
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.Add_Album,name='Add_Album' ),
    path('edit_Album/<int:id>',views.edit_Album,name='edit_Album' ),
    path('Delete_Album/<int:id>',views.Delete_Album,name='Delete_Album' ),

]
