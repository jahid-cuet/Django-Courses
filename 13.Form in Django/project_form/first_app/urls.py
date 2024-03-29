from django.urls import path
from .import views
urlpatterns = [
  
    path('form/', views.form,name='form'),
    path('about/', views.about,name='about'),
    path('django_form/', views.PasswordValidation, name = "django_form"),
    
]
