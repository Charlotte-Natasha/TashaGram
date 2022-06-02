from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'gram/index.html', {})

def sign_up(request):
    return render(request, 'gram/signup.html', {})    
