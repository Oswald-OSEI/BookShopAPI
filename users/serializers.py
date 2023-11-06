from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = "__all__"
        write_only_fields = ['password']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        write_only_fields = ['password']