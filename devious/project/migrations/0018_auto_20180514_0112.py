# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_auto_20180514_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='supporter',
            field=models.IntegerField(null=True, verbose_name='支持人数'),
        ),
    ]
