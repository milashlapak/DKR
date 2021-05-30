from database.models import VisitorRecord
from rest_framework import serializers

class VisitorRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorRecord
        fields = '__all__'

class UserNameSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)