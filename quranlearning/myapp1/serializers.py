from rest_framework import serializers
from .models import CustomUser, Teacher, Student, Group, Lesson, Error

# Сериализатор для CustomUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'role']

# Сериализатор для Teacher
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'email', 'phone']

# Сериализатор для Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'group']

# Сериализатор для Group
class GroupSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()  # Включаем информацию о преподавателе
    class Meta:
        model = Group
        fields = ['id', 'name', 'teacher', 'description']

# Сериализатор для Lesson
class LessonSerializer(serializers.ModelSerializer):
    group = GroupSerializer()  # Включаем информацию о группе
    class Meta:
        model = Lesson
        fields = ['id', 'group', 'topic', 'date', 'video_url', 'teacher_comments']

# Сериализатор для Error
class ErrorSerializer(serializers.ModelSerializer):
    student = StudentSerializer()  # Включаем информацию о студенте
    lesson = LessonSerializer()  # Включаем информацию о уроке
    class Meta:
        model = Error
        fields = ['id', 'student', 'lesson', 'description']
