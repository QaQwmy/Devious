# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_remove_project_members'),
        ('users', '0002_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSupprot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('add_time', models.DateField(verbose_name='支持时间', default=datetime.datetime.now)),
                ('project', models.ForeignKey(verbose_name='支持的项目', to='project.Project')),
                ('user', models.ForeignKey(verbose_name='支持者', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户支持',
                'verbose_name_plural': '用户支持',
            },
        ),
    ]
