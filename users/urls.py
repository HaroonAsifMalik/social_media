from django.contrib import admin
from django.urls import path , include
from . import views

# app_name = "users"
urlpatterns = [
    path( '', views.SignIn , name='signin'),
    path( 'dashbord/' , views.Dashbord, name='dashbord' ),
    path( 'signup/' , views.SignUp , name='signup'),
    path('profile/<str:username>' , views.Profile , name='profile'),    
    path('profile/<str:username>/edit/', views.EditProfile , name='editprofile'),
    path('logout' , views.LogOut , name='logout')
]