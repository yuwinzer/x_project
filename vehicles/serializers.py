from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Vehicle


class VehicleModelSerializer(HyperlinkedModelSerializer):
   class Meta:
       model = Vehicle
       fields = '__all__'