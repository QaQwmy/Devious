# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_usercreate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userflower',
            name='company',
            field=models.ForeignKey(to='project.Project', verbose_name='关注的公司'),
        ),
    ]
