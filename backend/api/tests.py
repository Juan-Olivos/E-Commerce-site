from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
# Create your tests here.

class getUsers(TestCase):
    def test_something(self):
        print(User.objects.all())
    
    def test_something2(self):
        print(Order.objects.all())
    
    