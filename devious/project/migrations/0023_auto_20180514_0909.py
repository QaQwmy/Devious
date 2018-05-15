# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0022_returngoods_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='types',
            field=models.CharField(verbose_name='发票', max_length=20, choices=[('0', '无发票'), ('1', '个人发票'), ('2', '自定义发票')]),
        ),
    ]
