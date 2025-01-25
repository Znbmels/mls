from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Настройка схемы API
schema_view = get_schema_view(
    openapi.Info(
        title="Quran Learning API",
        default_version="v1",
        description="API для платформы обучения Корану",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@quranlearning.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),  # Админка
    path("api/", include("myapp1.urls")),  # Основные API
    path("api/schema/", schema_view.without_ui(cache_timeout=0), name="schema"),  # JSON схема
    path("api/docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"),  # Swagger UI
    path("api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc"),  # Redoc UI
]
