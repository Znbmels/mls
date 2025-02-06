from django.contrib import admin
from .models import CustomUser, Teacher, Student, Group, Lesson, Error

admin.site.register(CustomUser)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Lesson)
admin.site.register(Error)
