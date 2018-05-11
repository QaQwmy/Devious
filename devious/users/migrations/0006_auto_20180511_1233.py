# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.BigIntegerField(verbose_name='手机号码'),
        ),
    ]
