from django.db import models


class Resource(models.Model):
    value = models.IntegerField()


class SubResource(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)