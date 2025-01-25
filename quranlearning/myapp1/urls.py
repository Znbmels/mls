from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeacherViewSet, StudentViewSet, GroupViewSet, LessonViewSet, ErrorViewSet

# Создаем роутер
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'errors', ErrorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Все маршруты для API
]
