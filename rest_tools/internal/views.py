from rest_framework import viewsets, response
from rest_framework.decorators import action

from rest_tools.internal.models import Resource, SubResource
from rest_tools.internal.serializers import ResourceSerializer, SubResourceSerializer
from rest_tools.views.mixins import ParentViewSetMixin


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class SubResourceViewSet(ParentViewSetMixin,
                         viewsets.ModelViewSet):
    queryset = SubResource.objects.all()
    serializer_class = SubResourceSerializer

    parent_lookup_url_kwarg = 'resource_pk'
    parent_field = 'resource'

    parent_viewset = ResourceViewSet
    inherit_permissions = True
