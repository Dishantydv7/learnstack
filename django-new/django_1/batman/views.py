from django.shortcuts import render
from .models import ALL_CHAI

# Create your views here.

def dishant(request):
    chais = ALL_CHAI.objects.all()
    return render(request , 'batman/dishant.html' , {'chais' : chais})
