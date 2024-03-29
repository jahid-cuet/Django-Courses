from django.urls import path
from .import views

urlpatterns = [

    # path('add/', Add_Post ,name='add_Post'),
    path('add/', views.AddPostCreateView.as_view(),name='Add_Post'),
    path('edit/<int:id>',views.EditPostView.as_view(),name='edit_Post'),
    # path('delete/<int:id>',views.delete_Post ,name='delete_Post'),
    path('delete/<int:id>',views.DeletePostView.as_view(),name='delete_Post'),
    path('details/<int:id>/', views.DetailPostView.as_view(), name='detail_post'),
   
]