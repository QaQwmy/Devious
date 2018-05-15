# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_auto_20180514_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='returngoods',
            name='number',
            field=models.IntegerField(verbose_name='回报数量', null=True),
        ),
    ]
