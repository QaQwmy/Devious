# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_auto_20180514_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='supportmoney',
            field=models.BigIntegerField(null=True, verbose_name='支持的金额'),
        ),
    ]
