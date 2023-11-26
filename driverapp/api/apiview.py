from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from account.models import User
from .serializers import *
from driverapp.models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from account.api.serializers import *

class UserDriverInfo(APIView):
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser]
    def get(self , request):
        user = User.objects.filter(is_bus_driver=True)
        for user in user:
            if request.user == user:
                serializer = UserSerializer(user)
                return Response(serializer.data , status=status.HTTP_200_OK)
            else:
                return Response({'error':'the information is not true'} , status=status.HTTP_400_BAD_REQUEST)
            
class UserDriverUpdate(APIView):
    serializer_class = UserUpdateSerializer
    parser_classes = [MultiPartParser]
    def put(self , request):
        user = request.user
        seri = UserUpdateSerializer(user , data=request.data , partial=True)
        if seri.is_valid():
            seri.save()
            return Response(seri.data , status=status.HTTP_200_OK)
        return Response(seri.errors , status=status.HTTP_400_BAD_REQUEST)
    
class DriverCarInfoCreate(APIView):
    serializer_class = BusInformationSerializer
    parser_classes = [MultiPartParser]
    def post(self , request):
        if request.user.is_bus_driver == True:
            data = request.data
            user = request.user
            serializer = BusInformationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.validated_data['user'] = user
                serializer.save()
                return Response(serializer.data , status=status.HTTP_200_OK)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        return Response({'response':'this request is not private'})
    
class CarInformationUpdateView(APIView):
    serializer_class = BusInformationSerializer
    parser_classes = [MultiPartParser]
    def put(self , request , id):
        if request.user.is_bus_driver == True:
            carinfo = get_object_or_404(BusInformation , id=id)
            data = request.data
            serializer = BusInformationSerializer(carinfo , data=request.data , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_200_OK)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        return Response({'response':'this request is not private'})
    
class CarListView(APIView):
    serilaizer_class = BusInformation
    parser_classes = [MultiPartParser]
    def get(self , request):
        bus_info = BusInformation.objects.filter(user=request.user)
        serializer = BusInformationSerializer(bus_info , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

class CarDetailView(APIView):
    serializer_class = BusInformationSerializer
    parser_classes = [MultiPartParser]
    def get(self , request , id):
        queryset = get_object_or_404(BusInformation , id=id)
        serializer = BusInformationSerializer(queryset)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
class DeleteCarView(APIView):
    serializer_class = BusInformationSerializer
    parser_classes = [MultiPartParser]
    def delete(self , request , id):
        car_info = get_object_or_404(BusInformation , id=id)
        if request.user == car_info.user:
            car_info.delete()
            return Response({'response':'deleted'})
    
class CreateCommentView(APIView):
    serializer_class = CommentSerializer
    parser_classes = [MultiPartParser]
    def post(self , request , id):
        data = request.data
        bus = get_object_or_404(BusInformation , id=id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['car_post'] = bus
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

