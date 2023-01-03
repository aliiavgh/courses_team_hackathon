import datetime

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from applications.purchases.models import Purchase
from applications.purchases.permissions import IsPurchaseOwner
from applications.purchases.serializers import PurchaseSerializer

@method_decorator(cache_page(60*60), name='dispatch')
class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsPurchaseOwner]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(student=self.request.user)
        return queryset


class PurchaseConfirmAPIView(APIView):
    @staticmethod
    def get(request, confirmation_code):
        purchase = get_object_or_404(Purchase, confirmation_code=confirmation_code)

        if not purchase.is_confirm:
            purchase.is_confirm = True
            today_date = datetime.date.today()
            purchase.status = 'in_process'
            purchase.save(update_fields=['is_confirm', 'status'])
            return Response({'message': 'You have been added to the course!'}, status=status.HTTP_200_OK)
        return Response({'message': 'You are already on the course!'}, status=status.HTTP_400_BAD_REQUEST)
