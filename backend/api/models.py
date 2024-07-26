from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name

class TestItem(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
