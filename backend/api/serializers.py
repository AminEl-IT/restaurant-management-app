from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'  # Prend tous les champs du model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Password jamais en lecture

    def create(self, validated_data):
        # Hash le password automatiquement
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

# Explication : Les serializers convertissent tes models Python en JSON pour l'API (et vice-versa).#