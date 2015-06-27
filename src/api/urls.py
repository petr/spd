# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from api.views import TaskViewSet

router = DefaultRouter()
router.register('tasks', TaskViewSet, 'task')

urlpatterns = router.urls
