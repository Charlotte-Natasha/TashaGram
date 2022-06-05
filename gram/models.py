from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    caption = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.caption + "\n" + self.description

class Image(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='media/images')
    caption = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='post_dislikes')

    def __str__(self): 
        return self.caption + "\n" + self.description

