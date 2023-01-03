from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile


class RegisterProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100)
    password2 = serializers.CharField(min_length=6, write_only=True, required=True)

    class Meta:
        model = Profile
        fields = ['email', 'password', 'password2']

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')
        if p1 != p2:
            raise serializers.ValidationError('Паспорт не верный')
        return attrs
