from django.http import HttpResponse
from django.shortcuts import render 


def home(request):
    return render(request, 'index.html')

def home2(request):
    return HttpResponse("Hello, Django 2!")

def home3(request):
    return HttpResponse("Hello, Django 3!")
