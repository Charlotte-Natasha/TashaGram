from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class PostForm(forms.ModelForm):
    class Meta:  
        model = Post
        fields = '__all__'

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = '__all__'

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        


