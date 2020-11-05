from django.shortcuts import render, redirect
from . import forms
from . import models
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
def home(request):
	return render(request,'home.html')
def place(request):
    return render(request,'place.html')
def login(request):
    if request.user.is_authenticated:
        return HttpResponse("you are already logged in")
    else:
        if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,
             password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/home/')
            else:
                return render(request, 'login.html', {'err': 'Wrong credentials provided'})
        else:
            return render(request, 'login.html', {'err': ''})

def logoutView(request):
    logout(request)
    return redirect('/login')

def signup(request):
    if request.method=='POST':
        form=forms.SignupForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            models.Profile(
            user=User.objects.get(username=form.cleaned_data.get('username')),
            phone=form.cleaned_data.get('phone'),
            city=form.cleaned_data.get('city')
            ).save()
            return redirect('/home')
        else:
            return render(request,'signup.html',{'form':form})
    else:
        form=forms.SignupForm()
    print(form)
    return render(request,'signup.html',{'form':form})
