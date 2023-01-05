from django.urls import path

from .views import ChangePasswordApiView

urlpatterns = [
    path('change_password/', ChangePasswordApiView.as_view()),
]
