from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def category(request):
    return render(request,"kalavya_backend/category.html")

def add_new_category(request):
    return render(request,"kalavya_backend/add-new-category.html")