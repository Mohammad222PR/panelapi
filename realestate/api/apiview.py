from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from realestate.models import *
from rest_framework.parsers import MultiPartParser
from account.api.serializers import UserSerializer , UserUpdateSerializer

class UserRealeStateInfo(APIView):
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser]
    def get(self , request):
        user = User.objects.filter(is_realestate=True)
        for user in user:
            if request.user == user:
                serializer = UserSerializer(user)
                return Response(serializer.data , status=status.HTTP_200_OK)
            else:
                return Response({'error':'the information is not true'} , status=status.HTTP_400_BAD_REQUEST)
            
class UserRealeStateUpdate(APIView):
    serializer_class = UserUpdateSerializer
    parser_classes = [MultiPartParser]
    def put(self , request):
        user = request.user
        seri = UserUpdateSerializer(user , data=request.data , partial=True)
        if seri.is_valid():
            seri.save()
            return Response(seri.data , status=status.HTTP_200_OK)
        return Response(seri.errors , status=status.HTTP_400_BAD_REQUEST)

class PropertyInformationCreateView(APIView):
    serializer_class = PropertyInformationSerializer
    parser_classes = [MultiPartParser]
    def post(self , request):
        if request.user.is_realestate == True:
            data = request.data
            user = request.user
            serializer = PropertyInformationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.validated_data['user'] = user
                serializer.save()
                return Response(serializer.data , status=status.HTTP_200_OK)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        return Response({'response':'this request is not private'})
    
class PropertyInformationUppdateView(APIView):
    serializer_class = PropertyInformationSerializer
    parser_classes = [MultiPartParser]
    def put(self , request , id):
        if request.user.is_realestate == True:
            property_info = get_object_or_404(PropertyInformation , id=id)
            data = request.data
            serializer = PropertyInformationSerializer(property_info , data=request.data , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_200_OK)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        return Response({'response':'this request is not private'})
    
class PropertyInformationListView(APIView):
    serializer_class = PropertyInformationSerializer
    parser_classes = [MultiPartParser]
    def get(self , request):
        property_info = PropertyInformation.objects.filter(user=request.user)
        serializer = PropertyInformationSerializer(property_info , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

class PropertyInformationsDetailView(APIView):
    serializer_class = PropertyInformationSerializer
    parser_classes = [MultiPartParser]
    def get(self , request , id):
        property_info = get_object_or_404(PropertyInformation , id=id)
        serializer = PropertyInformationSerializer(property_info)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
class DeletePropertyInformationView(APIView):
    serializer_class = PropertyInformationSerializer
    parser_classes = [MultiPartParser]
    def delete(self , request , id):
        property_info = get_object_or_404(PropertyInformation , id=id)
        if request.user == property_info.user:
            property_info.delete()
            return Response({'response':'deleted'})
    
class CreateCommentView(APIView):
    serializer_class = CommentSerializer
    parser_classes = [MultiPartParser]
    def post(self , request , id):
        data = request.data
        property_info = get_object_or_404(PropertyInformation , id=id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['property_post'] = property_info
            serializer.validated_data['user'] = request.user
            serializer.save
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class DeleteCommentView(APIView):
    serializer_class = CommentSerializer
    parser_classes = [MultiPartParser]
    def delete(self , requset , id):
        comment = get_object_or_404(Comment , id=id)
        if requset.user == comment.user:
            comment.delete()
            return Response({'response':'deleted'})