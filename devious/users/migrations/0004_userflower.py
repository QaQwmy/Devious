# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_project_createdate'),
        ('users', '0003_usersupprot'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFlower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('add_time', models.DateField(verbose_name='关注的时间', default=datetime.datetime.now)),
                ('company', models.ForeignKey(verbose_name='关注的公司', to='project.Company')),
                ('user', models.ForeignKey(verbose_name='关注的人', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户关注',
                'verbose_name_plural': '用户关注',
            },
        ),
    ]
