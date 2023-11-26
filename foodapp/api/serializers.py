from rest_framework import serializers
from foodapp.models import Comment , ChefInformation
from account.models import User

class CommentSerializer(serializers.ModelSerializer):
    parent = serializers.IntegerField(required=False)
    user = serializers.SlugRelatedField(read_only=True , slug_field='phone')
    foog_post = serializers.SlugRelatedField(read_only=True , slug_field='car_name')
    class Meta:
        model = Comment
        fields = ('__all__')

class ChefInfoSerializer(serializers.ModelSerializer):
    what_can_cook = serializers.SlugRelatedField(read_only=True , slug_field='name')
    class Meta:
        model = ChefInformation
        fields = ('__all__')

    def get_comment(self , obj):
        queryset = obj.comment.all()
        seri = CommentSerializer(queryset , many=True)
        return seri.data

