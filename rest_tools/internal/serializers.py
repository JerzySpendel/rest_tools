from rest_framework import serializers

from rest_tools.internal.models import Resource, SubResource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class SubResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubResource
        fields = '__all__'
