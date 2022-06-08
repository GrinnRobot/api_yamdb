from rest_framework import permissions
from users.models import User


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