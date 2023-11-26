from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import *
from account.models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser
from .phone import send_otp_via_phone
from django.contrib.auth import logout

class RegisterApiView(APIView):
    serializer_class = RegisterSerializer
    parser_classes = [MultiPartParser]
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            phone = data['phone']
            username = data['username']
            Full_name = data['Full_name']
            email = data['email']
            is_bus_driver = data['is_bus_driver']
            is_simple_user = data['is_simple_user']
            is_realestate = data['is_realestate']
            is_chef = data['is_chef']
            User.objects.get_or_create(phone=phone , username=username , Full_name=Full_name , email=email
            , is_realestate=is_realestate , is_simple_user=is_simple_user , is_bus_driver=is_bus_driver , is_chef=is_chef)
            user = User.objects.get(phone=phone)
            Token.objects.get_or_create(user=user)
            user.save()
            send_otp_via_phone(phone=phone)
            serializer.save()
            return Response({'response': 'Added'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoinApiView(APIView):
    serializer_class = LoginSerializer
    parser_classes = [MultiPartParser]
    def post(self , request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            phone = serializer.data['phone']
            user = User.objects.get(phone=phone)
            if user is not None:
                if user.otp == serializer.data['otp']:
                    user.otp = None
                    user.is_active = True
                    user.save()
                    return Response(data={
                        'Token': str(Token.objects.get(user=user)),
                    })
                
                return Response(data={
                    'otp_error': 'otp is wrong'
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors , status=status.HTTP_200_OK)
    
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': "Logout successful"})

class ProfileView(APIView):
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser]
    def get(self , request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data , status=status.HTTP_200_OK)

class ProfileUpdateView(APIView):
    serializer_class = UserUpdateSerializer
    parser_classes = [MultiPartParser]
    def put(self , request):
        user = request.user
        seri = UserUpdateSerializer(user , data=request.data , partial=True)
        if seri.is_valid():
            seri.save()
            return Response(seri.data , status=status.HTTP_200_OK)
        return Response(seri.errors , status=status.HTTP_400_BAD_REQUEST)