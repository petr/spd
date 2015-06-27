# -*- coding: utf-8 -*-

from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from tutorial.serializers import UserSerializer
from tutorial.models import User

__all__ = (
    'UserViewSet',
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
