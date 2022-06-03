from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from .email import send_welcome_email

# Create your views here.
def index(request):
    return render(request, 'gram/index.html', {})

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            send_welcome_email(name, email)
            
            login(request, user)
            return redirect('/login')

        messages.success(request, "Your account has been successfully created")
    
    else:
        form = RegisterForm() 
        
    return render(request, 'registration/signup.html', {'form':form})    

