from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from core.helpers import error_response, success_response
from .serializers import LoginSerializer, RefreshSerializer


# Create your views here.
class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return error_response(
                message="Invalid username or password.",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        username, password = (serializer.validated_data['username'],
                              serializer.validated_data['password'])
        user = authenticate(username=username, password=password)

        if user is None:
            return error_response(
                message="Invalid username or password.",
                status_code=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        data = {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh)
        }

        return success_response(
            message="Successfully logged in!",
            data=data,
            status_code=status.HTTP_200_OK
        )


class RefreshAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = RefreshSerializer(data=request.data)

        try:
            if serializer.is_valid():
                return success_response(
                    message="Successfully refreshed!",
                    data=serializer.validated_data
                )
            if not serializer.is_valid():
                return error_response(
                    message="Please double-check your input and try again.",
                    data=serializer.errors,
                )
        except TokenError as e:
            return error_response(
                message=str(e),
                status_code=status.HTTP_401_UNAUTHORIZED
            )

class TestAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response("dasdsa")