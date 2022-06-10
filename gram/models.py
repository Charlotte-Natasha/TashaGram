from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='images')
    description = models.TextField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

    class Meta:
        ordering = ['-created_at']    

class Profile(models.Model):
    author = models.OneToOneField(User,on_delete=models.CASCADE)
    followers = models.ManyToManyField(User,related_name="followers",blank=True)
    followings = models.ManyToManyField(User,related_name="followings",blank=True)
    profile_picture = models.ImageField( upload_to='profilepics')

class Reels(models.Model):
    reel = models.FileField(upload_to='reel')
    likes = models.ManyToManyField(User,blank=True)

class Story(models.Model):
    story = models.ImageField(upload_to="story")
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)