# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_auto_20180512_1025'),
        ('users', '0006_auto_20180511_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='project',
            field=models.ForeignKey(to='project.Project', null=True),
        ),
    ]
