from rest_framework import permissions


class IsMyAdminOrReadOnly(permissions.BasePermission):
    """Вход только для чтения, редактирование только для админа."""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.is_admin:
            return True
        return False
