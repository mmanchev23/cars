from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "profile_picture")


class CarSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    car_brand = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Car
        fields = ("id", "user", "car_brand", "created_at", "updated_at")
