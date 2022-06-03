from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'gram/index.html', {})

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/login')
    else:
        form = RegisterForm() 

        messages.success(request, "Your account has been successfully created")
    return render(request, 'registration/signup.html', {'form':form})    
