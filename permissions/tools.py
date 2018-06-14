import typing
from functools import wraps

from rest_framework.permissions import BasePermission


class PermissionTools:
    def __init_subclass__(cls, **kwargs):
        if kwargs.get('call_super'):
            PermissionTools.__decorate(cls)

    @staticmethod
    def _decorate_using_base_class(cls, base_classes):

        @wraps(cls.has_permission)
        def wrapper(self, *args, **kwargs):
            for base in base_classes:
                if not base.has_permission(self, *args, **kwargs):
                    return False

            return cls.has_permission(self, *args, **kwargs)

        return wrapper

    def __decorate(cls: typing.Type):
        bases = [base for base in cls.mro() if issubclass(base, BasePermission) and base is not cls]
        cls.has_permission = PermissionTools._decorate_using_base_class(cls, bases)
