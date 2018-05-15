# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20180512_0758'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='label',
            options={'verbose_name_plural': '标签', 'verbose_name': '标签'},
        ),
    ]
