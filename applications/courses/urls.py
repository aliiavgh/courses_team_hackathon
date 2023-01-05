from rest_framework.routers import DefaultRouter

from applications.courses.views import CourseViewSet, SubjectViewSet

router = DefaultRouter()
router.register('subjects', SubjectViewSet)
router.register('', CourseViewSet)

urlpatterns = router.urls
