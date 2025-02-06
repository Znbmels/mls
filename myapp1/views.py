from rest_framework import viewsets, permissions
from rest_framework.exceptions import NotFound
from django.contrib.auth import get_user_model
from .models import Teacher, Student, Group, Lesson, Error
from .serializers import (
    CustomUserSerializer,
    TeacherSerializer,
    StudentSerializer,
    GroupSerializer,
    LessonSerializer,
    ErrorSerializer
)
from .permissions import IsStudent, IsTeacher, IsAdmin, IsStudentOrTeacher

User = get_user_model()

# ViewSet для пользователя
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]  # Только администраторы могут управлять пользователями

# ViewSet для преподавателя
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated, IsTeacher | IsAdmin]  # Преподаватели и администраторы

# ViewSet для студента
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated, IsStudent | IsAdmin]  # Студенты и администраторы

# ViewSet для группы
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]  # Только администраторы могут управлять группами

# ViewSet для урока
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated, IsStudentOrTeacher]

    def get_queryset(self):
        user = self.request.user

        # Для студентов
        if user.role == 'student':
            if hasattr(user, 'student'):
                return Lesson.objects.filter(group=user.student.group)
            raise NotFound('У пользователя нет профиля студента.')

        # Для преподавателей
        if user.role == 'teacher':
            if hasattr(user, 'teacher'):
                return Lesson.objects.filter(teacher=user.teacher)
            raise NotFound('У пользователя нет профиля преподавателя.')

        # Для администраторов
        return self.queryset

# ViewSet для ошибки
class ErrorViewSet(viewsets.ModelViewSet):
    queryset = Error.objects.all()
    serializer_class = ErrorSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]  # Только администраторы могут управлять ошибками