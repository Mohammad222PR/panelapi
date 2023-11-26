from rest_framework import serializers
from realestate.models import Comment , PropertyInformation
from account.models import User

class CommentSerializer(serializers.ModelSerializer):
    parent = serializers.IntegerField(required=False)
    user = serializers.SlugRelatedField(read_only=True , slug_field='phone')
    property_post = serializers.SlugRelatedField(read_only=True , slug_field='car_name')
    class Meta:
        model = Comment
        fields = ('__all__')

class PropertyInformationSerializer(serializers.ModelSerializer):
    state = serializers.SlugRelatedField(read_only=True , slug_field='name')
    city = serializers.SlugRelatedField(read_only=True , slug_field='name')
    propertyModel = serializers.SlugRelatedField(read_only=True , slug_field='name')
    propertyType = serializers.SlugRelatedField(read_only=True , slug_field='name')
    propertyPossibilities = serializers.SlugRelatedField(read_only=True , slug_field='name')
    typeFloorProperty = serializers.SlugRelatedField(read_only=True , slug_field='name')
    heatingSystemProperty = serializers.SlugRelatedField(read_only=True , slug_field='name')
    coolingSystemProperty = serializers.SlugRelatedField(read_only=True , slug_field='name')
    selectionSans = serializers.SlugRelatedField(read_only=True , slug_field='name')
    kitchenEquipment = serializers.SlugRelatedField(read_only=True , slug_field='name')
    welfarePossibilities = serializers.SlugRelatedField(read_only=True , slug_field='name')
    entertainmentPossibilities = serializers.SlugRelatedField(read_only=True , slug_field='name')
    otherSpacesResidence = serializers.SlugRelatedField(read_only=True , slug_field='name')
    environmentalContext = serializers.SlugRelatedField(read_only=True , slug_field='name')
    bedCount = serializers.SlugRelatedField(read_only=True , slug_field='name')
    roomPossibilities = serializers.SlugRelatedField(read_only=True , slug_field='name')
    typeOwnership = serializers.SlugRelatedField(read_only=True , slug_field='name')
    class Meta:
        model = PropertyInformation
        fields = ('__all__')

    def get_comment(self , obj):
        queryset = obj.comment.all()
        seri = CommentSerializer(queryset , many=True)
        return seri.data

