# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userflower'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='收货地址')),
                ('phone', models.IntegerField(verbose_name='手机号码')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='收货人')),
            ],
            options={
                'verbose_name': '收货地址',
                'verbose_name_plural': '收货地址',
            },
        ),
    ]
