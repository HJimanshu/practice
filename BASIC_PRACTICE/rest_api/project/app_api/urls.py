
from django.urls import path,include
from rest_framework import routers
from .views import ComapanyViewset,EmployeeViewset


router=routers.DefaultRouter()
router.register(r'companies',ComapanyViewset)
router.register(r'employees',EmployeeViewset)

urlpatterns = [
    path('', include(router.urls))
  
]
