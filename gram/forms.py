from django import forms
from django.contrib.auth.models import User
from .models import *

class PostForm(forms.ModelForm):
    class Meta:  
        model = Post
        fields = ['image', 'caption', 'author', 'description']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'photo':''}   

