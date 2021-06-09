from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('',views.index,name='index'),
    path("signup",views.signup,name='signup'),
    path("login",views.Handlelogin,name='Handlelogin'),
    path("logout",views.Handlelogout,name='Handlelogout'),
    path("cart",views.cart,name='cart'),
    path("updateprofile",views.updateprofile,name='updateprofile'),
]