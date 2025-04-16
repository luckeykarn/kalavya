from django.contrib import admin
from .views import category,add_new_category
from django.urls import path

urlpatterns = [
    path('',category,name="category"),
    path('add/',add_new_category,name="add_new_category"),    

]