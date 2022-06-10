from rest_framework import permissions

from .models import User


class IsAdmin(permissions.BasePermission):
    """Вход только для админа."""
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.is_admin:
            return True
        return False


class IsMyAdminOrReadOnly(permissions.BasePermission):
    """Вход только для чтения, редактирование только для админа."""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.is_admin:
            return True
        return False


class IsStaffOrAuthorOrReadOnly(permissions.BasePermission):
    """
    Вход только для чтения, редактирование только для админа,
    модератора или автора.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            if ((request.user == obj.author)
                    or (request.user.role in (User.ADMIN, User.MODER))):
                return True
        return False
