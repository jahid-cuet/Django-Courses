from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [

    path('details/<int:id>/', views.DetailPostView.as_view(), name='detail_post'),

    path('cars/<int:car_id>/buy/', views.buy_car, name='buy_car'),
]

