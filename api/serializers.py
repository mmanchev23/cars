from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "photo")


class CarBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarBrand
        fields = "__all__"


class CarModelSerializer(serializers.ModelSerializer):

    car_brand = serializers.SlugRelatedField(slug_field="name", queryset=CarBrand.objects.all())
    
    class Meta:
        model = CarModel
        fields = ("id", "is_deleted", "deleted_at", "name", "created_at", "updated_at", "car_brand")


class UserCarSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())
    car_brand = serializers.SlugRelatedField(slug_field="name", queryset=CarBrand.objects.all())
    car_model = serializers.SlugRelatedField(slug_field="name", queryset=CarModel.objects.all())
    
    class Meta:
        model = UserCar
        fields = ("id", "is_deleted", "deleted_at", "first_reg", "odometer", "created_at", "user", "car_brand", "car_model")


class CarSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())
    car_brand = serializers.SlugRelatedField(slug_field="name", queryset=CarBrand.objects.all())
    
    class Meta:
        model = Car
        fields = ("id", "is_deleted", "deleted_at", "user", "car_brand", )
