from django.db import models
from drivers.models import Driver
# Create your models here.

class Vehicle(models.Model):
    id  = models.IntegerField(primary_key=True)
    driver_id  = models.ForeignKey(Driver, on_delete=models.SET_NULL,null=True, related_name='vehicle')
    make  = models.CharField(max_length=64)
    model  = models.CharField(max_length=64)
    plate_number  = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)