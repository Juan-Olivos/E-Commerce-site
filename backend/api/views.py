from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializers import *
from .models import *

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # anyone can create a user profile
    permission_classes = [AllowAny]

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    # all the products on the website should be viewed by anyone (need not be user)
    permission_classes = [AllowAny]

class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    # a product can only be added by an admin, not by a user
    permission_classes = [IsAdminUser]

class ListCreateTestItemView(generics.ListCreateAPIView):
    queryset = TestItem.objects.all()
    serializer_class = TestItemSerializer

    # only a user should be able to see and create their own item(eg. their cart)
    permission_classes = [IsAuthenticated]