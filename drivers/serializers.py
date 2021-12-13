from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Driver


class DriverModelSerializer(HyperlinkedModelSerializer):
   class Meta:
       model = Driver
       fields = '__all__'