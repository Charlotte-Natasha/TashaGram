from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
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
    posts = Post.objects.all()
    if request.method == 'POST':
        post_id = request.POST.get('post-id')
        post = Post.objects.filter(id=post_id).first()

        if post and post.user == request.user:
            post.delete() 
        
    return render(request, 'gram/index.html', {'posts':posts, 'profile':profile}) 
    

#create profile and user signup
def sign_up(request):
    if request.method == 'POST':
    
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # password1 = request.POST['password1']
        image = request.FILES['image']
        
        user = User.objects.create_user(username=username, email=email, password=password)
        profile = Profile.objects.create(author=user, profile_picture=image)
        user.save()
        profile.save()

        if profile:
            messages.success(request,'Profile Created Please Login')
            return redirect('login')
    else:  
        return render(request, 'registration/signup.html', {})      

# def create_profile(request):
#     posts = Post.objects.all()

#     if request.method == 'POST':
#         post_id = request.POST.get('post-id')
#         post = Post.objects.filter(id=post_id).first()
#         if post and post.author == request.user:
#             post.delete()

#     return render(request, 'gram/create_profile.html') 
    
@login_required(login_url="/login")
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.description = request.user
            post.save()   
            return redirect('home')
    else:
        form = PostForm()  

    return render(request, 'gram/create_posts.html', {'form':form})

@login_required(login_url="/login")
def profile(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        post_id = request.POST.get('post-id')
        post = Post.objects.filter(id=post_id).first()
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
        if post and post.user == request.user:
            user_form = UpdateUserForm(request.POST, instance=request.user)    
            post.delete() 
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'prof_form': prof_form,
    }
    return render(request, 'gram/profile.html', context)    

@login_required(login_url="/login")
def search(request):
    search = request.GET['username']
    profiles = Profile.objects.filter(author__username__icontains=search)
    context = {'profiles':profiles}

    return render(request, 'gram/profile.html', context)

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

    