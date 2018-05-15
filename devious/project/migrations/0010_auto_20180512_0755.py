# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20180512_0534'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='label',
            options={'verbose_name_plural': '面包标签', 'verbose_name': '面包标签'},
        ),
        migrations.RemoveField(
            model_name='label',
            name='super_label',
        ),
        migrations.AddField(
            model_name='label',
            name='project',
            field=models.ForeignKey(verbose_name='项目名称', to='project.Project', null=True),
        ),
    ]
