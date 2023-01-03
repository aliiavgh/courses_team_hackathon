from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.purchases.views import PurchaseViewSet, PurchaseConfirmAPIView

router = DefaultRouter()
router.register('', PurchaseViewSet)

urlpatterns = [
    path('confirm/<uuid:confirmation_code>/', PurchaseConfirmAPIView.as_view()),
]

urlpatterns += router.urls
