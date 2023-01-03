from rest_framework import serializers


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=6)
    new_password_confirm = serializers.CharField(required=True, min_length=6)

    def validate(self, attrs):
        p1 = attrs.get('new_password')
        p2 = attrs.pop('new_password_confirm')
        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def validate_old_password(self, attrs):
        request = self.context.get('request')
        user = request.user
        if not user.check_password(attrs):
            raise serializers.ValidationError('Неверный старый пароль')
        return attrs

    def set_new_password(self):
        user = self.context.get('request').user
        password = self.validated_data.get('new_password')
        user.set_password(password)
        user.save()
