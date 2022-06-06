from django import forms
from django.contrib.auth.models import User
from .models import *

class PostForm(forms.ModelForm):
    class Meta:  
        model = Post
        fields = '__all__'

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'caption', 'description']
        labels = {'photo':''}   

