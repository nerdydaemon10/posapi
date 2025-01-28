from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.helpers import error_response
from .serializers import LoginSerializer


# Create your views here.
class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return error_response(
                message="Invalid username or password.",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        username, password = (serializer.data['username'],
                              serializer.data['password'])
        user = authenticate(username=username, password=password)

        if user is None:
            return error_response(
                message="Invalid username or password.",
                status_code=status.HTTP_401_UNAUTHORIZED
            )

