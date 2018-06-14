from unittest.mock import Mock

from rest_framework import permissions as r_permissions
from rest_framework import test

from permissions.logic import Or, And


class APerm(r_permissions.BasePermission):
    def has_permission(self, request, view):
        return True


class BPerm(r_permissions.BasePermission):
    def has_permission(self, request, view):
        return False


class TestLogicCombinations(test.APITestCase):
    def setUp(self):
        self.AorB = Or(APerm, BPerm)
        self.AandB = And(APerm, BPerm)
        self.request_mock, self.view_mock = Mock(), Mock()

    def test_aperm_or_bperm_should_be_true(self):
        self.assertEqual(self.AorB().has_permission(self.request_mock, self.view_mock), True)

    def test_aperm_and_bperm_should_be_false(self):
        self.assertEqual(self.AandB().has_permission(self.request_mock, self.view_mock), False)
