# from django.contrib.auth.models import User
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# # from rest_framework.permissions import AllowAny
# from .serializers import UserSerializer
# from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
# # from django.contrib.auth.hashers import make_password,check_password
# # from django.contrib.auth.hashers import 


# @api_view(['POST'])
# def register(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         User.objects.create_user(
#             username=serializer.validated_data['username'],
#             # password=make_password(serializer.validated_data['password']),
#             password=request.data['password'],  # You may want to handle this differently
#             email=serializer.validated_data.get('email')
#         )
#         return Response({'status': 'User created',}, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['POST'])
# # @permission_classes([AllowAny])
# def login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     if not username or not password:
#         return Response({"detail": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)
#     # user1=check_password(password,          make_password(serializer.validated_data['password'])),
# # )
#     # user = authenticate(username=username, password=password)
#     user = authenticate(username=username, password=password)
#     print(user)
#     if user is not None:
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key}, status=status.HTTP_200_OK)
#     return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)



from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
    serializer.save()
    user=User.objects.get(username=serializer.data['username'])
    token_obj , _=Token.objects.get_or_create(user=user)
        # User.objects.create_user(
        #     username=serializer.validated_data['username'],
        #     password=make_password(serializer.validated_data['password']),
        #     email=serializer.validated_data.get('email')
        # )
    return Response({'status': 'User created','payload':serializer.data,'token':str(token_obj),'message':'Your data is saved'}, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"detail": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=username, password=password)
    # print(user)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        # print(user)
        return Response({'token': token.key, 'message': 'Login successful'}, status=status.HTTP_200_OK)

    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
