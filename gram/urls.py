from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('create_posts/', views.post, name='posts'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('followers', views.followers, name='followers')
]