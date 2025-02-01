from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=16, required=True)
    password = serializers.CharField(max_length=16, required=True)

class RefreshSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(required=True)

    def validate(self, attrs):
        refresh_token = attrs["refresh_token"]
        refresh = RefreshToken(refresh_token)
        data = {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh)
        }

        return data