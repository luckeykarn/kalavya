from django.contrib import admin
from .views import dashboard
from django.urls import path

urlpatterns = [
    path('',dashboard,name="backend_dashboard"),

]