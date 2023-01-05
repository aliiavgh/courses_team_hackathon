from rest_framework.permissions import BasePermission


class StudentOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated(request.user)


class TeacherManagerOnly(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and (request.user.is_staff and request.user.is_active))


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
