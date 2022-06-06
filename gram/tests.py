from django.test import TestCase
from .models import *

# Create your tests here.
class Profile(TestCase):
    def setUp(self):
        self.new_user = User(username='natasha')
        self.new_user.save()
        self.new_profile = Profile(bio='test bio', owner=self.new_user, name='natasha' )
        self.new_profile.save()
        