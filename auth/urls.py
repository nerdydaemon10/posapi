from django.urls import path

from auth.views import LoginAPIView

urlpatterns = [
    path('', LoginAPIView.as_view())
]