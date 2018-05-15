# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0023_auto_20180514_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='returngoods',
            name='invoice',
            field=models.CharField(max_length=20, choices=[('0', '无发票'), ('1', '个人发票'), ('2', '自定义发票')], verbose_name='发票'),
        ),
    ]
