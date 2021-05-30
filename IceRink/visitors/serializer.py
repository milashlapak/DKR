from rest_framework import serializers
from django.contrib.auth.models import User

class VisitorRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2']

class VisitorLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)