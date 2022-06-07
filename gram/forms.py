from django import forms
from django.contrib.auth.models import User
from .models import *

class PostForm(forms.ModelForm):
    class Meta:  
        model = Post
        fields = '__all__'
        widgets = {
            
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


