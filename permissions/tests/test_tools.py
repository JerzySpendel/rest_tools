import unittest
from unittest.mock import Mock

from rest_framework import permissions as r_permissions

from permissions.tools import PermissionTools


class BasePerm(r_permissions.BasePermission):
    def has_permission(self, request, view):
        return False


class PermissionWithAutomaticSuperCall(PermissionTools, BasePerm, call_super=True):
    def has_permission(self, request, view):
        return True


class PermissionWithoutAutomaticSuperCall(PermissionTools, BasePerm, call_super=False):
    def has_permission(self, request, view):
        return True


class TestPermissionTools(unittest.TestCase):
    def setUp(self):
        self.request_mock = Mock()
        self.view_mock = Mock()

    def test_base_classes_have_been_checked(self):
        value = PermissionWithAutomaticSuperCall().has_permission(self.request_mock, self.view_mock)
        self.assertEqual(value, False)

    def test_base_classes_have_not_been_checked(self):
        value = PermissionWithoutAutomaticSuperCall().has_permission(self.request_mock, self.view_mock)
        self.assertEqual(value, True)
