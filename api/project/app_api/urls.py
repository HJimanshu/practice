from django.urls import path,include
from rest_framework import routers 
from app_api.views import Comapny1Viewset,Employee1Viewset



router=routers.DefaultRouter()
router.register(r'company1',Comapny1Viewset)
router.register(r'employee1',Employee1Viewset)
urlpatterns = [
    path('',include(router.urls))
]
