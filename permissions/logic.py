import typing
import operator

from rest_framework import permissions as r_permissions


BasePermissionClass = typing.Type[r_permissions.BasePermission]


def ApplyLogicFunction(operator):

    def PermissionWithLogicOperator(a_perm: BasePermissionClass, b_perm: BasePermissionClass):

        class NewPermission(r_permissions.BasePermission):

            def has_permission(self, request, view):
                return operator(
                    a_perm().has_permission(request, view),
                    b_perm().has_permission(request, view),
                )

            def has_object_permission(self, request, view, obj):
                return operator(
                    a_perm().has_permission(request, view, obj),
                    b_perm().has_permission(request, view, obj)
                )

        return NewPermission

    return PermissionWithLogicOperator


Or = ApplyLogicFunction(operator.or_)
And = ApplyLogicFunction(operator.and_)
