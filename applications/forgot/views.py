from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ForgotPasswordSerializer, ForgotPasswordCompleteSerializer


# Create your views here.
class ForgotPasswordApiView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response('Вам отправлен код восстановления ')


class ForgotPasswordCompleteApiView(APIView):
    def post(self, request):
        serializer = ForgotPasswordCompleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Ваш пароль успешно обновлен')
