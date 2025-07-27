from rest_framework import permissions

class ResumePermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if not user.is_authenticated:
            return False

        if user.role == 'admin':
            return True

        if user.role == 'hr':
            return request.method in permissions.SAFE_METHODS

        if user.role == 'candidate':
            return obj.user == user

        return False

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        if user.role == 'admin':
            return True

        if user.role == 'hr':
            return request.method in permissions.SAFE_METHODS

        if user.role == 'candidate':
            return True

        return False
