from functools import reduce
import typing
import operator

from rest_framework import permissions as r_permissions


BasePermissionClass = typing.Type[r_permissions.BasePermission]


def ApplyLogicFunction(operator):

    def make_reducer(*context, permission_function='has_permission'):
        def reducer(a, b):
            if isinstance(a, bool) and issubclass(b, r_permissions.BasePermission):
                return operator(a, getattr(b(), permission_function)(*context))

            return operator(
                getattr(a(), permission_function)(*context),
                getattr(b(), permission_function)(*context)
            )

        return reducer

    def PermissionWithLogicOperator(*permission_classes: typing.List[r_permissions.BasePermission]):

        class NewPermission(r_permissions.BasePermission):

            def has_permission(self, request, view):
                reducer = make_reducer(request, view, permission_function='has_permission')
                return reduce(reducer, permission_classes)

            def has_object_permission(self, request, view, obj):
                reducer = make_reducer(request, view, obj, permission_function='has_object_permission')
                return reduce(reducer, permission_classes)

        return NewPermission

    return PermissionWithLogicOperator


Or = ApplyLogicFunction(operator.or_)
And = ApplyLogicFunction(operator.and_)
