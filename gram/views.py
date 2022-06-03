from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'gram/index.html', {})

def sign_up(request):
    
    form = RegisterForm()

    return render(request, 'registration/signup.html', {'form':form})    
