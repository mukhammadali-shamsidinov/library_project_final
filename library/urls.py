
from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Library Api",
        default_version='v1',
        description="Get Post Put Delete http metodlari mavjud"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('books.urls')),
    path('django-auth/',include('rest_framework.urls')),
    path('api/v1/auth/',include('dj_rest_auth.urls')),
    path('api/v1/auth/register/',include('dj_rest_auth.registration.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0))
]
