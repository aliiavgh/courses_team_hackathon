from django.contrib.auth import get_user_model
from rest_framework import serializers

from .send_mail import send_confirmation_email

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100)
    password2 = serializers.CharField(min_length=6, write_only=True, required=True)
    is_teacher = serializers.BooleanField(required=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'is_teacher']

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')
        if p1 != p2:
            raise serializers.ValidationError('Паспорт не верный')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_confirmation_email(email=user.email, code=user.activation_code)

        return user
