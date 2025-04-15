from django.contrib import admin
from .views import product_backend
from django.urls import path

urlpatterns = [
    path('',product_backend,name="product_backend"),

]