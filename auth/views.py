from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from auth.serializers import LoginSerializer


# Create your views here.
class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        username, password = (serializer.data['username'],
                              serializer.data['password'])
        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                data={
                    'isSuccess': False,
                    'data': None,
                    'message': 'Invalid username or password',
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(data={"isSuccess": True, "data": None, "message": "Successfully logged in!"}, status=status.HTTP_200_OK)

