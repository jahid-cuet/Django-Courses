from django.urls import path
from .import views

urlpatterns = [

    path('Register/',views.Register,name='Register'),
    path('Login/',views.Login,name='Login'),
    path('Profile/',views.Profile,name='Profile'),
    path('Profile/PassChange',views.PassChange,name='PassChange'),
    path('Profile/edit_profile',views.edit_profile,name='edit_profile'),
    path('Logout/',views.Logout,name='Logout'),
    
   
]