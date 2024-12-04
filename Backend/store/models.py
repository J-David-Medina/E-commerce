from django.db import models

# Modelo para categorías de productos
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Modelo productos
class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Modelo para roles de usuarios
class Role(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Modelo para usuarios
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Modelo para estados de órdenes
class State(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Modelo para órdenes
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_order = models.DateField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id} - {self.user.name}"

# Modelo para detalles de órdenes
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    total_price = models.FloatField(default=0.0)

    def __str__(self):
        return f"OrderDetail {self.id} - {self.product.name}"
