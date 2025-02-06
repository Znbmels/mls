from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Teacher, Student, Group, Lesson, Error

User = get_user_model()

# Сериализатор для создания пользователя (используется Djoser)
class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'student')
        )
        return user

# Сериализатор для отображения пользователя
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']


class TeacherSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        teacher = Teacher.objects.create(user=user, **validated_data)
        return teacher

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)

        # Обновляем основные поля модели `Teacher`
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()

        # Если есть данные для `user`, обновляем их
        if user_data:
            user = instance.user  # Получаем связанного пользователя
            user.username = user_data.get('username', user.username)
            user.email = user_data.get('email', user.email)
            user.role = user_data.get('role', user.role)
            if 'password' in user_data:
                user.set_password(user_data['password'])  # Обновляем пароль, если он передан
            user.save()

        return instance

class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'group', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)

        # Обновляем основные поля модели `Student`
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.group = validated_data.get('group', instance.group)
        instance.save()

        # Если есть данные для `user`, обновляем их
        if user_data:
            user = instance.user  # Получаем связанного пользователя
            user.username = user_data.get('username', user.username)
            user.email = user_data.get('email', user.email)
            user.role = user_data.get('role', user.role)
            if 'password' in user_data:
                user.set_password(user_data['password'])  # Обновляем пароль, если он передан
            user.save()

        return instance

# Сериализатор для группы
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'teacher', 'description']


# Сериализатор для урока
class LessonSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField()  # Добавляем поле, чтобы показать имя преподавателя

    class Meta:
        model = Lesson
        fields = ['id', 'group', 'topic', 'date', 'video_url', 'teacher_comments', 'teacher']

# Сериализатор для ошибки
class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = ['id', 'student', 'lesson', 'description']