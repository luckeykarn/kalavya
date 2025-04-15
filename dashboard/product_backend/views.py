from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def product_backend(request):
    return render(request,"kalavya_backend/products.html")
