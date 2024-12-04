from django.urls import path, include
from rest_framework import routers
from store import views

router = routers.DefaultRouter()
router.register(r'', views.CategoryView, 'category')
router.register(r'', views.ProductView, 'products')
router.register(r'', views.RoleView, 'roles')
router.register(r'', views.UserView, 'users')
router.register(r'', views.StateView, 'states')
router.register(r'', views.OrderView, 'orders')
router.register(r'', views.OrderDetailView, 'orderdetails')


urlpatterns = [
    path("api/v1", include(router.urls))
]
