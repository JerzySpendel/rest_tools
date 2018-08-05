from rest_framework import permissions as r_permissions


def create_related_permissions(return_a, return_b, return_c):
    """
    Just a util to automatically create 3 related permission classes
    """

    class PermA(r_permissions.BasePermission):
        def has_permission(self, request, view):
            return return_a

    class PermB(PermA):
        def has_permission(self, request, view):
            return return_b

    class PermC(PermB):
        def has_permission(self, request, view):
            return return_c

    return PermA, PermB, PermC
