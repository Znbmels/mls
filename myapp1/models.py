from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return self.username

# Модель преподавателя
class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)  # Добавили поле user
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Модель студента
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Модель группы
class Group(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Модель уроков
class Lesson(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, default=1) #связь с учителем
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    date = models.DateTimeField()
    video_url = models.URLField(blank=True, null=True)
    teacher_comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.topic} ({self.group.name})"

# Модель ошибок обозначенный учителем
class Error(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"Ошибка {self.student.first_name} {self.student.last_name} в уроке {self.lesson.topic}"