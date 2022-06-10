from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('create_posts/', views.post, name='posts'),
    # path('createprofile/', views.create_profile, name='create_profile'),
    path('profile/', views.profile, name='profile'),
    path('like/', views.like_post, name='like_post'),
]