from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import RegisterProfileSerializer

User = get_user_model()


class ProfileApiView(APIView):
    def post(self, request):
        serializer = RegisterProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Вы успешно зарегистрировались.', status=status.HTTP_201_CREATED)
