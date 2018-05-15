# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_auto_20180513_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='follower',
            field=models.IntegerField(default=0, verbose_name='关注人数'),
        ),
    ]
