from django.contrib import admin
from .views import dashboard
from django.urls import path,include

urlpatterns = [
    path('',dashboard,name="backend_dashboard"),
    path('product_backend/',include("dashboard.product_backend.urls")),
    path('category/',include("dashboard.category.urls")),
    
]