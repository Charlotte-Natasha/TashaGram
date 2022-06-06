import profile
import re
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='images')
    caption = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.caption + "\n" + self.description

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name="followers", blank=True)
    followings = models.ManyToManyField(User, related_name="followings")
    profile_picture = models.ImageField(upload_to="profilepics")

    def __str__(self): 
        return self.user


class Image(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='media/images')
    caption = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='post_dislikes')

    def __str__(self): 
        return self.title

class FollowersCount(models.Model):
    follower = models.CharField(max_length=1000)
    user = models.CharField(max_length=1000)

    def __str__(self): 
        return self.user

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.CharField(max_length=1000)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title + "\n" + self.user