from rest_framework.permissions import BasePermission


class IsPurchaseOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH']:
            return request.user.is_authenticated and request.user == obj.student
        return request.user.is_authenticated and (request.user == obj.student or request.user.is_staff)
    