from django.urls import path, include
from rest_framework import routers
from store import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryView, 'category')
router.register(r'products', views.ProductView, 'products')
router.register(r'roles', views.RoleView, 'roles')
router.register(r'users', views.UserView, 'users')
router.register(r'states', views.StateView, 'states')
router.register(r'orders', views.OrderView, 'orders')
router.register(r'order-details', views.OrderDetailView, 'orderdetails')


urlpatterns = [
    path("api/v1/", include(router.urls))
]
