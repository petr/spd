# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='zip_code',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
