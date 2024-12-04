from rest_framework import viewsets
from .serializer import *
from .models import *
# Create your views here.

class CategoryView(viewsets.ModelViewSet):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()

class ProductView(viewsets.ModelViewSet):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()

class RoleView(viewsets.ModelViewSet):
  serializer_class = RoleSerializer
  queryset = Role.objects.all()

class UserView(viewsets.ModelViewSet):
  serializer_class = UserSerializer
  queryset = User.objects.all()

class StateView(viewsets.ModelViewSet):
  serializer_class = StateSerializer
  queryset = State.objects.all()

class OrderView(viewsets.ModelViewSet):
  serializer_class = OrderSerializer
  queryset = Order.objects.all()

class OrderDetailView(viewsets.ModelViewSet):
  serializer_class = OrderDetailSerializer
  queryset = OrderDetail.objects.all()
