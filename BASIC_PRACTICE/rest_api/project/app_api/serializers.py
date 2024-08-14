from rest_framework import serializers
from app_api.models import Company,Employee

#create serializer here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    Company_id=serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields= '__all__'
#Employee Serializer         
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields= '__all__'