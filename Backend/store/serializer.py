from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields  = '__all__'

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields  = '__all__'

class RoleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Role
    fields  = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields  = '__all__'

class StateSerializer(serializers.ModelSerializer):
  class Meta:
    model = State
    fields  = '__all__'

class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields  = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = OrderDetail
    fields  = '__all__'


