from rest_framework import serializers

from applications.purchases.models import Purchase
from applications.purchases.tasks import send_purchase_confirmation_email


class PurchaseSerializer(serializers.ModelSerializer):
    student = serializers.EmailField(required=False)

    class Meta:
        model = Purchase
        exclude = ('confirmation_code',)

<<<<<<< HEAD
    def create(self, validated_data):
=======
    @staticmethod
    def create(validated_data):
>>>>>>> demo
        course = validated_data['course']
        if course.status is False:
            raise serializers.ValidationError('Unfortunately, this course is no longer available.')
        course.places -= 1
        course.save(update_fields=['places'])

        purchase = Purchase.objects.create(**validated_data)
        send_purchase_confirmation_email.delay(purchase.student.email, purchase.confirmation_code)
        return purchase
