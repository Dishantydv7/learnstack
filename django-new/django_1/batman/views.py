from django.shortcuts import render
from .models import ALL_CHAI
from django.shortcuts import get_object_or_404

# Create your views here.

def dishant(request):
    chais = ALL_CHAI.objects.all()
    return render(request , 'batman/dishant.html' , {'chais' : chais})

def chai_detail(request , chai_id):
    chai = get_object_or_404(ALL_CHAI , pk=chai_id)
    return render(request , 'batman/chai_detail.html' , {'chai' : chai})
