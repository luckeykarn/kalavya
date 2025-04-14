from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def dashboard(request):
    return render(request,"kalavya_backend/index.html")