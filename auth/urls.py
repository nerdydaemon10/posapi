from django.urls import path

from .views import LoginAPIView, RefreshAPIView, TestAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('refresh/', RefreshAPIView.as_view()),
    path('test/', TestAPIView.as_view())
]