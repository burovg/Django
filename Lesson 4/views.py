from django.http import HttpResponse
from django.shortcuts import *
from django.views import View

def Hello(request):
    return HttpResponse("Welcome to Our page 2")

def Contact(request):
    return HttpResponse("Contact Page")

def HomePage(request):
    return render(request, 'HomePage.html')
