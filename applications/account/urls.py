from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterApiView, ActivationApiView, profile

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('profile/', profile),
    path('activate/<uuid:activation_code>/', ActivationApiView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
