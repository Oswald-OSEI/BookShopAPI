from rest_framework import serializers
from .models import CustomUser, LoginModel, Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["first_name", "middle_name", "last_name", "email", "tel_number", "Gender", "password"]
        write_only_fields = ['password']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginModel
        fields = ['email', 'password']
        write_only_fields = ['password']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['postal_address', 'house_address', 'City', 'region', 'country', 'profile_picture']