from django.urls import path
from .views import UserRegistrationView, UserLoginView,user_logout,Passchange
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('Logout/', user_logout, name='logout'),
    path('profile/', Passchange, name='profile' )
]