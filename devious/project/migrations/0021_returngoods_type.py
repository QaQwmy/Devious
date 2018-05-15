# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_returngoods_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='returngoods',
            name='type',
            field=models.CharField(default='0', choices=[('0', '实物回报'), ('1', '虚拟物品回报')], max_length=20, verbose_name='回报类型'),
        ),
    ]
