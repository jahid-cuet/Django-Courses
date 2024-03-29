from django.urls import path,include
from .import views

urlpatterns = [

    path('', views.home),
    path('Signup/', views.Signup,name='Signup'),
    path('Login/', views.Login,name='Login'),
    path('Profile/', views.Profile,name='Profile'),
    path('Logout/', views.Logout,name='Logout'),
    path('Passchange/', views.Passchange,name='Passchange'),
    path('pass_change2/', views.pass_change2,name='pass_change2'),
    
    

]