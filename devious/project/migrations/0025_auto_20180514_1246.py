# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0024_auto_20180514_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='supportmoney',
            field=models.BigIntegerField(verbose_name='支持的金额', null=True, default=0),
        ),
    ]
