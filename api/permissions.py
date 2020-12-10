from rest_framework.permissions import BasePermission



class IsOwnerOrReadOnly(BasePermission):
    def has_object_premission(self , reqest , veiw ,obj):
        return obj.Fname == reqest.Fname