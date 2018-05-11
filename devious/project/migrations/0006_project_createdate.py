# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_remove_project_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='createdate',
            field=models.DateField(verbose_name='创建项目的时间', default=datetime.datetime.now),
        ),
    ]
