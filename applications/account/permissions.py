from rest_framework.permissions import BasePermission


class StudentOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated(request.user, "students")


class TeacherManagerOnly(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and hasattr(request.user, 'teacher')
                and request.user.member.is_active
                and request.user.member.is_staff
                )

    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.groups.filter(name='Teacher').exists()

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.groups.filter(name='Teacher').exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.groups.filter(name='Teacher').exists()


# class StudentAndTeacherManagerOnly(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and (
#             hasattr(request.user, "students")
#             or (
#                 hasattr(request.user, "member")
#                 and request.user.member.is_active
#                 and request.user.member.is_manager
#             )
#         )
