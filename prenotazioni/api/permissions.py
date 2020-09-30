from rest_framework import permissions

class IsUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return  True
        return obj.prenotazione.user == request.user


class IsUserOrReadOnlyOrIsStaff(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return  True
        if request.user.is_staff:
            return  True
        return obj.user == request.user
