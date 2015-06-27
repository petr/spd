# -*- coding: utf-8 -*-

from rest_framework import serializers


__all__ = (
    'ImagePutSerializer',
    'TaskSerializer',
)


class ImagePutSerializer(serializers.Serializer):
    image = serializers.ImageField(write_only=True)


class TaskSerializer(serializers.Serializer):
    task_id = serializers.IntegerField()
