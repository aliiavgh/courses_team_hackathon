from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.purchases.views import PurchaseViewSet, PurchaseConfirmAPIView

router = DefaultRouter()
router.register('', PurchaseViewSet, basename='purchases')

urlpatterns = [
    path('confirm/<uuid:confirmation_code>/', PurchaseConfirmAPIView.as_view(), name='confirm'),
]

urlpatterns += router.urls
