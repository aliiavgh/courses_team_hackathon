from django.urls import path

from .views import ForgotPasswordApiView, ForgotPasswordCompleteApiView

urlpatterns = [
    path('forgot_password/', ForgotPasswordApiView.as_view()),
    path('forgot_password_complete/', ForgotPasswordCompleteApiView.as_view()),
]
