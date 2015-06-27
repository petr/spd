# -*- coding: utf-8 -*-

from rest_framework import serializers

from tutorial.models import User

__all__ = (
    'UserSerializer',
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'pk', 'email', 'zip_code', 'url')
