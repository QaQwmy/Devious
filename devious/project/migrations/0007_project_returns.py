# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_project_createdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='returns',
            field=models.CharField(verbose_name='回报内容', max_length=255, null=True),
        ),
    ]
