from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello eho is their")
    return render( request , "website/index.html")

def harish(request):
    return HttpResponse("hello gendu")