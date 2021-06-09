from django.shortcuts import render
from django.utils import timezone
from django.views.generic import CreateView,DetailView

# Create your views here.

def index(request):
    context ={}    
    return render(request,'DataAnalysis.html',context)
 
