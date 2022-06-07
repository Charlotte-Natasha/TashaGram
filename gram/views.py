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
@login_required(login_url="/login")
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
    

        if form.is_valid():
            user = form.save()
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            send_welcome_email(name, email)
            
        #     login(request, user)
        #     return redirect('/login')

    
    else:
        
        return render(request, 'registration/signup.html', {})     

@login_required(login_url="/login")
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.description = request.user
            post.save()   
            return redirect('/profile')
    else:
        form = PostForm()  

    return render(request, 'gram/create_posts.html', {'form':form})

def uploadok(request):
    return HttpResponse('upload successful')

@login_required(login_url="/login")
def profile(request):
        posts = Post.objects.all()
        # profile = Profile.objects.get(user=request.user)
        # comments = Comment.objects.filter(post=post).order_by('date')

        if request.method == 'POST':
            post_id = request.POST.get('post-id')
            post = Post.objects.filter(id=post_id).first()
            if post and post.user == request.user:
                post.delete() 


        return render(request, 'gram/profile.html', {'posts':posts, 'profile':profile, 'profile_of_user':True})     

@login_required(login_url="/login")
def search(request):
    search = request.GET['username']
    profiles = Profile.objects.filter(user__username__icontains=search)
    context = {'profiles':profiles}

    return render(request, 'gram/search.html', context)

# VIEW FOR FOLLOWING THE USER
@login_required(login_url="/login")
def follow(request,id,username):
    profile = Profile.objects.get(id=id)
    Login_profile = Profile.objects.get(user=request.user)
    if request.user in profile.followers.all():
        profile.followers.remove(request.user)
        Login_profile.followings.remove(profile.user)
    else:
        profile.followers.add(request.user)
        Login_profile.followings.add(profile.user)
    return redirect(f'/search?username={username}') 

# FUNCTION FOR LIKING THE POST
@login_required(login_url="/login")
def like_post(request,id):
    post = Post.objects.filter(id=id)
    if request.user in post[0].likes.all():
        post[0].likes.remove(request.user)
    else:
        post[0].likes.add(request.user)
    return redirect("index")       

def dashboard(request):
    
    return render(request, 'gram/dashboard.html', {})              


def comment(request):

    return render(request, 'gram/comment.html', {}) 
    