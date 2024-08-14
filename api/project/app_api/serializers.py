from rest_framework import serializers
from app_api.models import *

class Company1Serializer(serializers.HyperlinkedModelSerializer):
    comapany1_id=serializers.ReadOnlyField()
    class Meta:
        model= Company1
        fields='__all__'
class Employee1Serializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model= Employee1
        fields='__all__'