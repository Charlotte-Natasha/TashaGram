from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages
from .email import send_welcome_email
from .models import *

# Create your views here.
def index(request):
    return render(request, 'gram/index.html', {})

def sign_up(request):
    if request.method == 'POST':
        user = request.POST('user')
        username = request.POST('username')
        email = request.POST('email')
        password = request.POST('password')
        password1 = request.POST('password1')

        my_user = User.objects.create_user(username, email, password)
        my_user.save()

        messages.success(request, "Your account has been successfully created")

        return redirect('signup')

    #     if form.is_valid():
    #         user = form.save()
            # name = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # send_welcome_email(name, email)
            
        #     login(request, user)
        #     return redirect('/login')

    
    # else:
    #     form = form
        
    return render(request, 'registration/signup.html', {}) 

def post(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        post_id = request.POST.get('post-id')
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()  

    return render(request, 'gram/posts.html', {'posts':posts})