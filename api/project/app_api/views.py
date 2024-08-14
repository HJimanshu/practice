from django.shortcuts import render
from rest_framework import viewsets
from app_api.models import *
from app_api.serializers import Company1Serializer,Employee1Serializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class Comapny1Viewset(viewsets.ModelViewSet):
    queryset = Company1.objects.all()
    serializer_class = Company1Serializer
    
    # companies/{comapnyID}/employees/
    # for custom url
    @action(detail=True,methods=['get'])
    def employee1(self,request,pk=None):
        try:
           company= Company1.objects.get(pk=pk)
           emp=Employee1.objects.filter(company=company)
           emp_serializer=Employee1Serializer(emp,many=True,context={'request':request})
        #  print("Employee",pk,"company")
           return Response(emp_serializer.data)
        except Exception as e:
             return Response({
               'message':"Company might not exist !! Error"  
             }      )
             
    
class Employee1Viewset(viewsets.ModelViewSet):
    queryset = Employee1.objects.all()
    serializer_class = Employee1Serializer