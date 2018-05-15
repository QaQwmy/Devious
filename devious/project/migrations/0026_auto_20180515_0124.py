# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0025_auto_20180514_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.CharField(verbose_name='项目标签', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='supporter',
            field=models.IntegerField(verbose_name='支持人数', default=0, null=True),
        ),
    ]
