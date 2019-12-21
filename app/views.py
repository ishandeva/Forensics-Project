from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dashboard(request):
    return render(request,'app/index.html')

def upload(request):
    return render(request,'app/upload.html')

#def login (request):
#    return render(request,'app/login.html')
