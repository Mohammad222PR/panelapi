from rest_framework import serializers
from simpleuser.models import SimpleUserInformation
from account.models import User
class SimpleUserInformationSerializer(serializers.ModelSerializer):
    state = serializers.SlugRelatedField(read_only=True , slug_field='name')
    city = serializers.SlugRelatedField(read_only=True , slug_field='name')
    class Meta:
        model = SimpleUserInformation
        fields = ('__all__')

