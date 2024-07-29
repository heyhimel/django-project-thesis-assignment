from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='homepage'),
    path('login/', login, name='loginpage'),
    path('register/', register, name='registerpage'),
]
