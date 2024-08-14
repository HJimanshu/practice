from django.urls import path,include
from auth_app.views import register_view
urlpatterns = [
    path('',register_view,name='register'),
]