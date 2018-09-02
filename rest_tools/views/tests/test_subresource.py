from rest_framework import test, viewsets, serializers, status

from rest_tools.internal.models import Resource, SubResource
from rest_tools.internal.views import ResourceViewSet, SubResourceViewSet


class TestViewSets(test.APITestCase):
    def setUp(self):
        self.factory = test.APIRequestFactory()
        self.request = self.factory.get('')

        self.resource = Resource.objects.create(value=3)
        self.sub_resource = SubResource.objects.create(resource=self.resource)
        self.view = SubResourceViewSet.as_view({'get': 'retrieve'})

    def test_valid_get(self):
        response = self.view(self.request,
                             resource_pk=self.resource.pk,
                             pk=self.sub_resource.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_get(self):
        response = self.view(self.request,
                             resource_pk=self.resource.pk + 1,
                             pk=self.sub_resource.pk)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
