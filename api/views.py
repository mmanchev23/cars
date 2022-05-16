from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import viewsets, permissions

        
class UserView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)

        if self.object_list:
            return Response({f"{self.request.user.username}" : serializer.data})
        else:
            return Response({"Message" : "No user found!"})


class CarView(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, car_brand=self.request.GET.get("car_brand"))

    def perform_update(self, serializer):
        serializer.save(user=self.request.user, car_brand=self.request.GET.get("car_brand"))

    def get_queryset(self):
        return Car.objects.all()

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)

        if self.object_list:
            return Response({"Cars" : serializer.data})
        else:
            return Response({"Message" : "No cars found!"})