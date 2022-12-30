from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer, ProfileSerializer

User = get_user_model()


class RegisterApiView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Вы успешно зарегистрировались. Вам отправили код для активации', status=status.HTTP_201_CREATED)


@login_required
@transaction.atomic
def profile(request):
    if request.method == 'POST':
        user_serializer = RegisterSerializer(request.POST, instance=request.user)
        profile_serializer = ProfileSerializer(request.POST, instance=request.user.profile)
        if user_serializer.is_valid() and profile_serializer.is_valid():
            user_serializer.save()
            profile_serializer.save()
            return Response('Ваш профиль был успешно обновлен!')
        else:
            return Response('Пожалуйста, исправьте ошибки')
    else:
        user_serializer = RegisterSerializer(instance=request.user)
        profile_serializer = ProfileSerializer(instance=request.user.profile)
    return Response({
        'user_form': user_serializer,
        'profile_form': profile_serializer
    })


class ActivationApiView(APIView):

    def get(self, request, activation_code):
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response({'msg': 'Успешно'}, status=status.HTTP_200_OK)
