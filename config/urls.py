from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from config import settings

schema_view = get_schema_view(
    openapi.Info(
        title='Team hackathon',
        default_version='v1',
        description='Courses'
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/courses/', include('applications.courses.urls')),
    path('api/v1/comments/', include('applications.feedback.urls')),
    path('api/v1/purchases/', include('applications.purchases.urls')),
    path('swagger/', schema_view.with_ui('swagger')),
    path('api/v1/account/', include('applications.account.urls')),
    path('api/v1/forgot/', include('applications.forgot.urls')),
    path('api/v1/change/', include('applications.change.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
