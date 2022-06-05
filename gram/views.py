from django.http import HttpResponse
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
        # fname = request.POST['fname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        user = User.objects.create_user( username=username, email=email, password=password )
        user.save()
        

        messages.success(request, "Your account has been successfully created")

        return redirect('/login')
    

    #     if form.is_valid():
    #         user = form.save()
            # name = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # send_welcome_email(name, email)
            
        #     login(request, user)
        #     return redirect('/login')

    
    else:
        
        return render(request, 'registration/signup.html', {}) 

def profile(request):
        posts = Post.objects.all()

        if request.method == 'POST':
            post_id = request.POST.get('post-id')
            post = Post.objects.filter(id=post_id).first()
            if post and post.author == request.user:
                post.delete() 

        return render(request, 'gram/profile.html', {'posts':posts})    

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()   
            return redirect('/profile')
    else:
        form = PostForm()  

    return render(request, 'gram/create_posts.html', {'form':form})

def dashboard(request):
    current_user = request.POST.get('user')
    logged_in_user = request.user.username

    return render(request, 'gram/dashboard.html', {'current_user':current_user})

def uploadok(request):
    return HttpResponse('upload successful')               

def followers(request):
    pass 