from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or request.user.is_superuser:
            return True
        return request.user == obj.creator


class FavoritePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action == 'mark_as_favorite':
            return obj.creator != request.user
        return True