from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=16, required=True)
    password = serializers.CharField(max_length=16, required=True)