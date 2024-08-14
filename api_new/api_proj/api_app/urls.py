# from django.urls import path,include
# from api_app.views import *
# from rest_framework import routers 
# from api_app.views import SignupViewset
# from rest_framework.routers import DefaultRouter
# from rest_framework.


# router=routers.DefaultRouter()
# router.register(r'register',SignupViewset)
# # router.register(r'login',LoginViewSet)
# urlpatterns = [
#     path('',include(router.urls)),
#     path('api-token-auth/', CustomAuthToken.as_view())
    # path('login/', login, name='login'),
    #  re_path('login', views.login),
    # path('',signup,name='signup'),
    # path('',login,name='login'),
    # path('',login,name='login'),
# ]






# router=routers.DefaultRouter()
# router.register(r'company1',Comapny1Viewset)
# router.register(r'employee1',Employee1Viewset)
# urlpatterns = [
#     path('',include(router.urls))
# ]

from django.urls import path
from .views import register,login


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    # Other URLs...
]
