from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from foodapp.models import *
from rest_framework.parsers import MultiPartParser
from account.api.serializers import UserSerializer, UserUpdateSerializer


class UserChefInfo(APIView):
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser]

    def get(self, request):
        user = User.objects.filter(is_chef=True)
        for user in user:
            if request.user == user:
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": "the information is not true"},
                    status=status.HTTP_400_BAD_REQUEST,
                )


class UserChefUpdate(APIView):
    serializer_class = UserUpdateSerializer
    parser_classes = [MultiPartParser]

    def put(self, request):
        user = request.user
        seri = UserUpdateSerializer(user, data=request.data, partial=True)
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=status.HTTP_200_OK)
        return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)


class ChefInformationCreateView(APIView):
    serializer_class = ChefInfoSerializer
    parser_classes = [MultiPartParser]

    def post(self, request):
        if request.user.is_chef == True:
            data = request.data
            user = request.user
            serializer = ChefInfoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.validated_data["user"] = user
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"response": "this request is not private"})


class ChefInformationUppdateView(APIView):
    serializer_class = ChefInfoSerializer
    parser_classes = [MultiPartParser]

    def put(self, request, id):
        if request.user.is_chef == True:
            chef_info = get_object_or_404(ChefInformation, id=id)
            data = request.data
            serializer = ChefInfoSerializer(chef_info, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"response": "this request is not private"})


class ChefInformationListView(APIView):
    serializer_class = ChefInfoSerializer
    parser_classes = [MultiPartParser]

    def get(self, request):
        chef_info = ChefInformation.objects.filter(user=request.user)
        serializer = ChefInfoSerializer(chef_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChefInformationsDetailView(APIView):
    serializer_class = ChefInfoSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, id):
        chef_info = get_object_or_404(ChefInformation, id=id)
        serializer = ChefInfoSerializer(chef_info)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteChefInformationView(APIView):
    serializer_class = ChefInfoSerializer
    parser_classes = [MultiPartParser]

    def delete(self, request, id):
        chef_info = get_object_or_404(ChefInformation, id=id)
        if request.user == chef_info.user:
            chef_info.delete()
            return Response({"response": "deleted"})


class CreateCommentView(APIView):
    serializer_class = CommentSerializer
    parser_classes = [MultiPartParser]

    def post(self, request, id):
        data = request.data
        food_info = get_object_or_404(ChefInformation, id=id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["food_post"] = food_info
            serializer.validated_data["user"] = request.user
            serializer.save
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCommentView(APIView):
    serializer_class = CommentSerializer
    parser_classes = [MultiPartParser]

    def delete(self, requset, id):
        comment = get_object_or_404(Comment, id=id)
        if requset.user == comment.user:
            comment.delete()
            return Response({"response": "deleted"})
