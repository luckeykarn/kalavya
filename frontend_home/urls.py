from django.contrib import admin
from .views import home
from django.urls import path

urlpatterns = [
    path('',home,name="home"),

]