from django.contrib import admin 
from .models import Category, Product, Role, User, State, Order, OrderDetail

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Role)
admin.site.register(User)
admin.site.register(State)
admin.site.register(Order)
admin.site.register(OrderDetail)
