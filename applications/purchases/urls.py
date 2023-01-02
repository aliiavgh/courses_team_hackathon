from rest_framework.routers import DefaultRouter

from applications.purchases.views import PurchaseViewSet

router = DefaultRouter()
router.register('', PurchaseViewSet)

urlpatterns = router.urls
