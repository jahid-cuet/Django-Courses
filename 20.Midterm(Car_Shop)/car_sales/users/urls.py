
from django.urls import path
from .import views

urlpatterns = [
    
    path('Signup/', views.Register,name='Signup'),
    path('Login/', views.Login,name='Login'),
    path('Profile/',views.Profile,name='Profile'),
    path('Logout/',views.Logout,name='Logout'),
     path('profile/edit', views.edit_profile, name='edit_profile'),
 
]
