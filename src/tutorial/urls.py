# -*- coding: utf-8 -*-

from rest_framework.routers import DefaultRouter

from tutorial.views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, 'user')

urlpatterns = router.urls
