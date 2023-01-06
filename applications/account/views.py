from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from loguru import logger

from .serializers import RegisterSerializer

User = get_user_model()

logger.add('log.log', format='{time} {level} {message}', level='ERROR', serialize=True)


class RegisterApiView(APIView):
    @logger.catch
    def post(self, request):

        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Вы успешно зарегистрировались.Вам отправили код для активации', status=status.HTTP_201_CREATED)


class ActivationApiView(APIView):
    @logger.catch
    def get(self, request, activation_code):
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response('Вы успешно зарегистрировались.Вам отправили код для активации', status=status.HTTP_200_OK)
