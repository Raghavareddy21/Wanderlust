from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
def home(request):
	return render(request,'home.html')
def place(request,pk):
    return render(request,'place.html')
