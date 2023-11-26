from rest_framework import serializers
from driverapp.models import *
from account.models import User

class CommentSerializer(serializers.ModelSerializer):
    parent = serializers.IntegerField(required=False)
    user = serializers.SlugRelatedField(read_only=True , slug_field='phone')
    car_post = serializers.SlugRelatedField(read_only=True , slug_field='car_name')
    class Meta:
        model = Comment
        fields = ('__all__')

class BusInformationSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True , slug_field='phone')
    device_color = serializers.SlugRelatedField(read_only=True , slug_field='name')
    device_type = serializers.SlugRelatedField(read_only=True , slug_field='name')
    car_type = serializers.SlugRelatedField(read_only=True , slug_field='name')
    comment = serializers.SerializerMethodField()
    class Meta:
        model = BusInformation
        fields = ('__all__')

    def get_comment(self , obj):
        queryset = obj.comments.all()
        seri = CommentSerializer(queryset , many=True)
        return seri.data