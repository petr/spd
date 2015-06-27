# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from api.serializers import ImagePutSerializer, TaskSerializer

__all__ = (
    'TaskViewSet',
)


class TaskViewSet(ViewSet):
    serializer_class = ImagePutSerializer

    def create(self, request, *args, **kwargs):
        serializer = ImagePutSerializer(data=request.FILES)
        serializer.is_valid(raise_exception=True)
        return Response({'id': 1234, 'status': 'processing', }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        serializer = TaskSerializer(data={'task_id': pk})
        serializer.is_valid(raise_exception=True)
        if pk == '1234':
            response = {
                'id': 1234,
                'status': 'success',
            }
            return Response(response, status=status.HTTP_200_OK)

        return Response({}, status=status.HTTP_404_NOT_FOUND)
