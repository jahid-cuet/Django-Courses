from django.urls import path
from .import views
# from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('Register/',views.Register,name='Register'),
    # path('Login/',views.Login,name='Login'),
    path('Login/', views.UserLoginView.as_view(), name='Login'),
    path('Profile/',views.Profile,name='Profile'),
    path('Profile/PassChange',views.PassChange,name='PassChange'),
    path('Profile/edit_profile',views.edit_profile,name='edit_profile'),
    path('Logout/',views.Logout,name='Logout'),
    # path('Logout/',views.LogoutView.as_view(),name='Logout'), For class based viewed
    
   
]