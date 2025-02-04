from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStudentOrTeacher
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from rest_framework.exceptions import NotFound
from .models import Teacher, Student, Group, Lesson, Error
from .serializers import (
    CustomUserSerializer,
    TeacherSerializer,
    StudentSerializer,
    GroupSerializer,
    LessonSerializer,
    ErrorSerializer
)

User = get_user_model()

# ViewSet для пользователя
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# ViewSet для преподавателя
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# ViewSet для студента
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# ViewSet для группы
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# ViewSet для урока
class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsStudentOrTeacher]

    def get_queryset(self):
        user = self.request.user

        def get_queryset(self):
            user = self.request.user

            if user.role == 'student':
                # Если у студента нет профиля, выбрасываем ошибку
                if hasattr(user, 'student'):
                    return Lesson.objects.filter(group=user.student.group)
                else:
                    raise NotFound('Student profile not found.')

            if user.role == 'teacher':
                # Если у учителя нет профиля, выбрасываем ошибку
                if hasattr(user, 'teacher'):
                    return Lesson.objects.filter(teacher=user.teacher)
                else:
                    raise NotFound('Teacher profile not found.')

            # Если роль админа, показываем все уроки
            return Lesson.objects.al

# ViewSet для ошибки
class ErrorViewSet(viewsets.ModelViewSet):
    queryset = Error.objects.all()
    serializer_class = ErrorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]