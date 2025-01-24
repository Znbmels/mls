from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, StudentViewSet, GroupViewSet, LessonViewSet, ErrorViewSet

# Создание маршрутизатора и регистрация ViewSet
router = DefaultRouter()
router.register('teachers', TeacherViewSet, basename='teacher')
router.register('students', StudentViewSet, basename='student')
router.register('groups', GroupViewSet, basename='group')
router.register('lessons', LessonViewSet, basename='lesson')
router.register('errors', ErrorViewSet, basename='error')

# Подключение маршрутов маршрутизатора
urlpatterns = [
    path('', include(router.urls)),
]
