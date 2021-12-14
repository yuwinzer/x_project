from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Vehicle
from .serializers import VehicleModelSerializer


class VehicleModelViewSet(ModelViewSet):
   queryset = Vehicle.objects.all()
   serializer_class = VehicleModelSerializer