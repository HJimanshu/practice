
from django.urls import path
from .views import create,register

urlpatterns = [
    path("",create,name="create"),
    path("register/",register,name="register"),
]
