"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Team hackathon',
        default_version='v1',
        description='Courses'
    ),
    public=True
)


from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('applications.account.urls')),
    path('api/v1/courses/', include('applications.courses.urls')),
<<<<<<< HEAD
    path('api/v1/comments/', include('applications.feedback.urls')),
    path('api/v1/purchases/', include('applications.purchases.urls'))
=======
    path('swagger/', schema_view.with_ui('swagger')),
    path('api/v1/account/', include('applications.account.urls')),
    path('api/v1/forgot/', include('applications.forgot.urls')),
    path('api/v1/change/', include('applications.change.urls')),
>>>>>>> 3fadcee9b3fdb1e8af498ca4b836e322ffd26284
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
