from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializers import *
from .models import *
from django.db.models import F
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # anyone can create a user profile
    permission_classes = [AllowAny]

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # all the products on the website should be viewed by anyone (need not be user)
    permission_classes = [AllowAny]

class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # a product can only be added by an admin, not by a user
    permission_classes = [IsAdminUser]

# class ListCreateTestItemView(generics.ListCreateAPIView):
#     queryset = TestItem.objects.all()
#     serializer_class = TestItemSerializer

    # only a user should be able to see and create their own item(eg. their cart)
    permission_classes = [IsAuthenticated]

class ListOrderItemsView(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        order = Order.objects.filter(customer_id = self.request.user.id, is_completed = False)
        if not order:
            return OrderItem.objects.none()
        
        return OrderItem.objects.filter(order_id = order[0].id)
    
    def create(self, request, *args, **kwargs):
        # need to find the order since this cannot be passed from frontend
        order = Order.objects.get(customer_id = self.request.user.id, is_completed = False)

        if not order:
            order = Order.objects.create(customer=self.request.user, is_completed=False)
        
        # must be passed from frontend
        product_id = request.data.get('product')
        product = Product.objects.get(id=product_id)

        # pass from frontend, default = 1
        quantity = int(request.data.get('quantity'))

        # check if this product exists as order_item in this order
        try:
            order_item = OrderItem.objects.get(order=order,product=product)
            created = False
            order_item.quantity=F('quantity')+quantity
            order_item.save()
        except:
            order_item = OrderItem.objects.create(product=product, order=order)
            order_item.quantity=F('quantity')+quantity
            order_item.save()
            created = True

        order_item.refresh_from_db()

        serializer = self.get_serializer(order_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)