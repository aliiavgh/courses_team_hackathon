import datetime

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from applications.purchases.models import Purchase
from applications.purchases.permissions import IsPurchaseOwner
from applications.purchases.serializers import PurchaseSerializer


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer()
    permission_classes = [IsPurchaseOwner]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(student=self.request.user)
        return queryset


class OrderConfirmAPIView(APIView):
    @staticmethod
    def get(request, code):
        purchase = get_object_or_404(Purchase, confirmation_code=code)

        if not purchase.is_confirm:
            purchase.is_confirm = True
            today_date = datetime.date.today()
            purchase.status = 'in_process' \
                if today_date in datetime.timedelta(purchase.course.start_date, purchase.course.end_date) \
                else 'waiting'
            purchase.save(update_fields=['is_confirm', 'status'])
            return Response({'message': 'You have been added to the course!'}, status=status.HTTP_200_OK)
        return Response({'message': 'You are already on the course!'}, status=status.HTTP_400_BAD_REQUEST)