from django.db import models

__all__ = (
    'User',
)


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=20, null=True)
    zip_code = models.CharField(max_length=6, null=True)
