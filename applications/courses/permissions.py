from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsCourseOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.method in ['PUT', 'PATCH']:
            return request.user.is_authenticated and request.user == obj.teacher
        return request.user.is_authenticated and request.user == obj.teacher and request.user.is_teacher
