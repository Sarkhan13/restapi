from rest_framework import permissions



class isAdminorRead(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin =  super().has_permission(request, view)

        return request.method in permissions.SAFE_METHODS or is_admin
    

class isAuthorReadonly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        elif request.user == obj.user or request.user.is_superuser:
            return True
    