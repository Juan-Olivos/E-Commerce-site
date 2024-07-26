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

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class TestItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestItem
        fields = '__all__'