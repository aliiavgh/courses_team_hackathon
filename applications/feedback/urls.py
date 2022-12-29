from rest_framework.routers import DefaultRouter

from applications.feedback.views import CommentViewSet

router = DefaultRouter()
router.register('', CommentViewSet)

urlpatterns = router.urls
