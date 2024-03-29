
from django.urls import path
from .import views

urlpatterns = [

    path('',views.Add_Musician,name='Add_Musician' ),
    path('Register/',views.Register,name='Register'),
    # path('Login/',views.Login,name='Login'),
    path('Login/', views.UserLoginView.as_view(), name='Login'),
    path('Profile/',views.Profile,name='Profile'),
    path('Logout/',views.Logout,name='Logout'),
]
