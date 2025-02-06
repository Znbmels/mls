from rest_framework.permissions import BasePermission

class IsStudent(BasePermission):
    """
    Разрешение для студентов.
    """
    def has_permission(self, request, view):
        return request.user.role == 'student'

class IsTeacher(BasePermission):
    """
    Разрешение для преподавателей.
    """
    def has_permission(self, request, view):
        return request.user.role == 'teacher'

class IsAdmin(BasePermission):
    """
    Разрешение для администраторов.
    """
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsStudentOrTeacher(BasePermission):
    """
    Разрешение для студентов и преподавателей.
    """
    def has_permission(self, request, view):
        return request.user.role in ['student', 'teacher']