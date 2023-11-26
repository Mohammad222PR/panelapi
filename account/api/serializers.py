from django.forms import ValidationError
from rest_framework import serializers
from account.models import User

boolean_choices = (
  (True, 'Yes'),
  (False, 'No'),
)


class RegisterSerializer(serializers.Serializer):
    phone = serializers.IntegerField()
    email = serializers.CharField()
    username = serializers.CharField()
    Full_name = serializers.CharField()
    is_bus_driver = serializers.ChoiceField(choices=boolean_choices)
    is_simple_user = serializers.ChoiceField(choices=boolean_choices)
    is_realestate = serializers.ChoiceField(choices=boolean_choices)
    is_chef = serializers.ChoiceField(choices=boolean_choices)

    def create(self, validated_data):
        phone = validated_data['phone']
        email = validated_data['email']
        username = validated_data['username']
        Full_name = validated_data['Full_name']
        is_bus_driver = validated_data['is_bus_driver']
        is_simple_user = validated_data['is_simple_user']
        is_realestate = validated_data['is_realestate']
        is_chef = validated_data['is_chef']
        User.objects.get_or_create(phone=phone , username=username , Full_name=Full_name , email=email
        , is_realestate=is_realestate , is_bus_driver=is_bus_driver , is_simple_user=is_simple_user , is_chef=is_chef)
        user = User.objects.get(phone=phone)
        return user
    
class LoginSerializer(serializers.Serializer):
    phone = serializers.IntegerField()
    otp = serializers.CharField(required=False)

    def create(self, validated_data):
        phone = validated_data['phone']
        User.objects.get_or_create(phone=phone)
        user = User.objects.get(phone=phone)
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)
    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','Full_name')