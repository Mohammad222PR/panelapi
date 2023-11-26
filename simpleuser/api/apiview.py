from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from simpleuser.models import *
from rest_framework.parsers import MultiPartParser
from account.api.serializers import UserSerializer , UserUpdateSerializer

class UserSimpleUserInfo(APIView):
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser]
    def get(self , request):
        user = User.objects.filter(is_simple_user=True)
        for user in user:
            if request.user == user:
                serializer = UserSerializer(user)
                return Response(serializer.data , status=status.HTTP_200_OK)
            else:
                return Response({'error':'the information is not true'} , status=status.HTTP_400_BAD_REQUEST)
            
class UserSimpleUserUpdate(APIView):
    serializer_class = UserUpdateSerializer
    parser_classes = [MultiPartParser]
    def put(self , request):
        user = request.user
        seri = UserUpdateSerializer(user , data=request.data , partial=True)
        if seri.is_valid():
            seri.save()
            return Response(seri.data , status=status.HTTP_200_OK)
        return Response(seri.errors , status=status.HTTP_400_BAD_REQUEST)

class SimpleUserInformationCreateView(APIView):
    serializer_class = SimpleUserInformationSerializer
    parser_classes = [MultiPartParser]
    def post(self , request):
        if request.user.is_simple_user == True:
            data = request.data
            user = request.user
            serializer = SimpleUserInformationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.validated_data['user'] = user
                serializer.save()
                return Response(serializer.data , status=status.HTTP_200_OK)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        return Response({'response':'this request is not private'})
    
class SimpleUserInformationUppdateView(APIView):
    serializer_class = SimpleUserInformationSerializer
    parser_classes = [MultiPartParser]
    def put(self , request , id):
        if request.user.is_simple_user == True:
            simple_user_info = get_object_or_404(SimpleUserInformation , id=id)
            data = request.data
            serializer = SimpleUserInformationSerializer(simple_user_info , data=request.data , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_200_OK)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        return Response({'response':'this request is not private'})
    
class SimpleUserInformationListView(APIView):
    serializer_class = SimpleUserInformationSerializer
    parser_classes = [MultiPartParser]
    def get(self , request):
        simple_user_info = SimpleUserInformation.objects.filter(user=request.user)
        serializer = SimpleUserInformationSerializer(simple_user_info , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

class SimpleUserInformationDetailView(APIView):
    serializer_class = SimpleUserInformationSerializer
    parser_classes = [MultiPartParser]
    def get(self , request , id):
        simple_user_info = get_object_or_404(SimpleUserInformation , id=id)
        serializer = SimpleUserInformationSerializer(simple_user_info)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
class DeleteSimpleUserInformationView(APIView):
    serializer_class = SimpleUserInformationSerializer
    parser_classes = [MultiPartParser]
    def delete(self , request , id):
        property_info = get_object_or_404(SimpleUserInformation , id=id)
        if request.user == property_info.user:
            property_info.delete()
            return Response({'response':'deleted'})