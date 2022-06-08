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


class IsAdminOrReadOnly(permissions.BasePermission):
    """Вход только для чтения, редактирование только для админа."""
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user.is_authenticated and request.user.is_admin)
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_admin


class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Вход только для чтения, редактирование только для админа или модератора.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role in (User.ADMIN, User.MODER)


class IsCatEatsBats(permissions.BasePermission):
    """Вход строго запрещён."""
    def has_permission(self, request, view):
        return False
