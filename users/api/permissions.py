from rest_framework import serializers
from rest_framework import permissions



class IsOwnProfileOrReadOnly(permissions.BasePermission):
#    user = serializers.StringRelatedField(read_only=True)

    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return  True

#        return obj.username == str(request.user)
        return obj.username == request.user.username
