from django.urls import path
from bookstore import views
from django.shortcuts import render,redirect

urlpatterns = [
    path('register/', views.registeruser),
    path('login/', views.loginuser),
]
