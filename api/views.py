from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import viewsets, permissions

        
class UserView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return User.objects.all()

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)

        if self.object_list:
            return Response({"users" : serializer.data})
        else:
            return Response({"message" : "No users found!"})


class CarBrandView(viewsets.ModelViewSet):
    serializer_class = CarBrandSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CarBrand.objects.all()

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)

        if self.object_list:
            return Response({"brands" : serializer.data})
        else:
            return Response({"message" : "No brands found!"})


class CarModelView(viewsets.ModelViewSet):
    serializer_class = CarModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CarModel.objects.all()

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)

        if self.object_list:
            return Response({"models" : serializer.data})
        else:
            return Response({"message" : "No models found!"})


class UserCarView(viewsets.ModelViewSet):
    serializer_class = UserCarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserCar.objects.all()

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)

        if self.object_list:
            return Response({"results" : serializer.data})
        else:
            return Response({"message" : "No results found!"})


class CarView(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Car.objects.all()

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)

        if self.object_list:
            return Response({"cars" : serializer.data})
        else:
            return Response({"message" : "No cars found!"})
