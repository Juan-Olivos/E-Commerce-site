from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=False, blank=False)
    #image

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    total_price = models.FloatField(default=0.0)

    def __str__(self):
        return f'Cart for {self.customer.username}'

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

