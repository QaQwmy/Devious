# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_auto_20180512_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='returngoods',
            name='desc',
            field=models.CharField(max_length=100, null=True, verbose_name='回报简述'),
        ),
    ]
