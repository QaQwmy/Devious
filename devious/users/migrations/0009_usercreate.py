# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0024_auto_20180514_1101'),
        ('users', '0008_auto_20180512_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCreate',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='关注的时间')),
                ('project', models.ForeignKey(to='project.Project', verbose_name='创建的项目')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='创建项目的人')),
            ],
            options={
                'verbose_name_plural': '创建项目表',
                'verbose_name': '创建项目表',
            },
        ),
    ]
