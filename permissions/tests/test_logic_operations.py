from unittest.mock import Mock

import pytest
from rest_framework import permissions as r_permissions

from permissions.logic import Or, And


class APerm(r_permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return True


class BPerm(r_permissions.BasePermission):
    def has_permission(self, request, view):
        return False

    def has_object_permission(self, request, view, obj):
        return False


boolean_to_class = {
    True: APerm,
    False: BPerm,
}


class TestLogicCombinations:
    def setup_method(self):
        self.request_mock, self.view_mock, self.obj_mock = Mock(), Mock(), Mock()

    @pytest.mark.parametrize('first_perm,second_perm,third_perm,expected', [
        (boolean_to_class[True], boolean_to_class[True], boolean_to_class[True], True),
        (boolean_to_class[True], boolean_to_class[False], boolean_to_class[True], True),
        (boolean_to_class[False], boolean_to_class[True], boolean_to_class[True], True),
        (boolean_to_class[False], boolean_to_class[False], boolean_to_class[True], True),
        (boolean_to_class[True], boolean_to_class[True], boolean_to_class[False], True),
        (boolean_to_class[True], boolean_to_class[False], boolean_to_class[False], True),
        (boolean_to_class[False], boolean_to_class[True], boolean_to_class[False], True),
        (boolean_to_class[False], boolean_to_class[False], boolean_to_class[False], False)
    ])
    def test_or(self, first_perm, second_perm, third_perm, expected):
        AorBorC = Or(first_perm, second_perm, third_perm)
        assert AorBorC().has_permission(self.request_mock, self.view_mock) is expected
        assert AorBorC().has_object_permission(self.request_mock, self.view_mock, self.obj_mock) is expected

    @pytest.mark.parametrize('first_perm,second_perm,third_perm,expected', [
        (boolean_to_class[True], boolean_to_class[True], boolean_to_class[True], True),
        (boolean_to_class[True], boolean_to_class[False], boolean_to_class[True], False),
        (boolean_to_class[False], boolean_to_class[True], boolean_to_class[True], False),
        (boolean_to_class[False], boolean_to_class[False], boolean_to_class[True], False),
        (boolean_to_class[True], boolean_to_class[True], boolean_to_class[False], False),
        (boolean_to_class[True], boolean_to_class[False], boolean_to_class[False], False),
        (boolean_to_class[False], boolean_to_class[True], boolean_to_class[False], False),
        (boolean_to_class[False], boolean_to_class[False], boolean_to_class[False], False)
    ])
    def test_and(self, first_perm, second_perm, third_perm, expected):
        AandBandC = And(first_perm, second_perm, third_perm)
        assert AandBandC().has_object_permission(self.request_mock, self.view_mock, self.obj_mock) is expected
        assert AandBandC().has_permission(self.request_mock, self.view_mock) is expected
