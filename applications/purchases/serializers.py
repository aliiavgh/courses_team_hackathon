from rest_framework import serializers

from applications.purchases.models import Purchase
from applications.purchases.tasks import send_purchase_confirmation_email


class PurchaseSerializer(serializers.ModelSerializer):
    student = serializers.EmailField(required=False)

    class Meta:
        model = Purchase
        exclude = ('confirmation_code',)

    def validate(self, attrs):
        course_access = attrs['course'].is_available
        if course_access is False:
            raise serializers.ValidationError('Unfortunately, this course is no longer available.')
        return attrs

    @staticmethod
    def create(validated_data):
        course = validated_data['course']
        course.available_places -= 1
        course.save(update_fields=['available_places'])

        purchase = Purchase.objects.create(**validated_data)
        send_purchase_confirmation_email.delay(email=purchase.student.email, title=purchase.course.title,
                                               price=purchase.course.price, confirmation_code=purchase.confirmation_code)
        return purchase
