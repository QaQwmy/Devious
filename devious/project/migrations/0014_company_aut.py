# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_returngoods_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='aut',
            field=models.CharField(choices=[('0', '未认证'), ('1', '已认证')], max_length=100, null=True, verbose_name='认证状态', default='0'),
        ),
    ]
