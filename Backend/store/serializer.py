from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
  class meta:
    models = Category
    firlds  = '__all__'

class ProductSerializer(serializers.ModelSerializer):
  class meta:
    models = Product
    firlds  = '__all__'

class RoleSerializer(serializers.ModelSerializer):
  class meta:
    models = Role
    firlds  = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class meta:
    models = User
    firlds  = '__all__'

class StateSerializer(serializers.ModelSerializer):
  class meta:
    models = State
    firlds  = '__all__'

class OrderSerializer(serializers.ModelSerializer):
  class meta:
    models = Order
    firlds  = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
  class meta:
    models = OrderDetail
    firlds  = '__all__'


