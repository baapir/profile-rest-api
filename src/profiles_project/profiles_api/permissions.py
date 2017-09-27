from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profiles"""

    def has_object_permission(self, request, view, obj):
        """chek user is trying to edit their own profiles"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    """allows user to update thier own status"""

    def has_object_permission(self, request, view, obj):
        """chek the user is trying to update thier own status"""

        if request.method in permissions.SAFE_METHOD:
            return True

        return obj.user.id == request.user.id
