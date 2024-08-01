from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}  # no one can know what the password is

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer
    product_name = serializers.CharField(source='product.name', read_only=True)
    class Meta:
        model = OrderItem
        fields = ['id', 'product_name','product', 'order', 'quantity']

class Order(serializers.ModelSerializer):
    customer = UserSerializer()
    item = OrderItemSerializer()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'item']

class OrderSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)
    items = OrderItemSerializer(many=True, source='orderitem_set', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'date_ordered', 'is_completed', 'total_price', 'items']

class CheckoutSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()

    def validate_order_id(self, value):
        try:
            order = Order.objects.get(id=value, is_completed=False)
        except Order.DoesNotExist:
            raise serializers.ValidationError("Order does not exist or is already completed.")
        return value
