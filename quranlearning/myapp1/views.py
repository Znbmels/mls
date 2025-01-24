from rest_framework.viewsets import ModelViewSet
from .models import Teacher, Student, Group, Lesson, Error
from .serializers import (
    TeacherSerializer,
    StudentSerializer,
    GroupSerializer,
    LessonSerializer,
    ErrorSerializer,
)

# ViewSet для модели Teacher
class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

# ViewSet для модели Student
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# ViewSet для модели Group
class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# ViewSet для модели Lesson
class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

# ViewSet для модели Error
class ErrorViewSet(ModelViewSet):
    queryset = Error.objects.all()
    serializer_class = ErrorSerializer
