from rest_framework import serializers
from .models import Teacher, Student, Group, Lesson, Error

# Сериализатор для модели Teacher
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

# Сериализатор для модели Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

# Сериализатор для модели Group
class GroupSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)  # Вложенный сериализатор для учителя

    class Meta:
        model = Group
        fields = '__all__'

# Сериализатор для модели Lesson
class LessonSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)  # Вложенный сериализатор для группы

    class Meta:
        model = Lesson
        fields = '__all__'

# Сериализатор для модели Error
class ErrorSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)  # Вложенный сериализатор для студента
    lesson = LessonSerializer(read_only=True)   # Вложенный сериализатор для урока

    class Meta:
        model = Error
        fields = '__all__'
