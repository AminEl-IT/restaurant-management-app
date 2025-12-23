from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet, basename='restaurant')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.login, name='login'),
]

#Explication : Les URLs définissent les chemins de ton API (ex: /api/restaurants/).