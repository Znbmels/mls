from rest_framework import permissions

class IsTeacher(permissions.BasePermission):
    """
    Разрешение только для учителей.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'teacher'

class IsStudent(permissions.BasePermission):
    """
    Разрешение только для студентов.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'

class IsTeacherOrReadOnly(permissions.BasePermission):
    """
    Разрешение для учителей на все действия, для студентов — только на чтение.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return request.user.is_authenticated and request.user.role == 'teacher'

class IsStudentOrTeacher(permissions.BasePermission):
    """
    Разрешает доступ только студентам к своим урокам и учителям к своим урокам.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Если студент — он должен видеть только уроки своей группы
        if user.role == 'student':
            return obj.group == user.student.group

        # Если учитель — он должен видеть только свои уроки
        if user.role == 'teacher':
            return obj.teacher == user.teacher

        return False  # Для всех остальных доступ запрещён
