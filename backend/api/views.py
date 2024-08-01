from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializers import *
from .models import *
from django.db.models import F
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .utils import process_payment

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
        quantity = int(request.data.get('quantity', 1))

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
    

class RUDOrderItemView(generics.RetrieveUpdateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()

    # assuming id will always be present
    def update(self, request, *args, **kwargs):
        order_item_id = kwargs.get('pk')

        order_item = OrderItem.objects.get(id=order_item_id, order__customer_id=self.request.user.id, order__is_completed=False)

        # assume frontend passes action to increase or decrease item quantity
        action = request.data.get('action')
        if action == 'add':
            order_item.quantity = F('quantity') + 1
        elif action == 'sub':
            order_item.quantity = F('quantity') - 1
        else:
            return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)

        order_item.save()
        order_item.refresh_from_db()

        serializer = self.get_serializer(order_item)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteCartItemView(generics.DestroyAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()

class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid():
            order_id = serializer.validated_data['order_id']
            order = Order.objects.get(id=order_id)

            if not order.orderitem_set.exists():
                return Response({"error": "No items in the order"}, status=status.HTTP_400_BAD_REQUEST)

            # Calculate total price
            total_price = sum(item.product.price * item.quantity for item in order.orderitem_set.all())
            order.total_price = total_price
            order.save()

            # Process payment (33% random chance of failed order)
            payment_successful = process_payment(order)

            if payment_successful:
                order.is_completed = True
                order.save()
                return Response(OrderSerializer(order).data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Credit Card Authorization Failed"}, status=status.HTTP_402_PAYMENT_REQUIRED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)