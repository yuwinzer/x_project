from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Driver
from .serializers import DriverModelSerializer


class DriverModelViewSet(ModelViewSet):
   queryset = Driver.objects.all()
   serializer_class = DriverModelSerializer