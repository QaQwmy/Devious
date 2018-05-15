# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0021_returngoods_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='returngoods',
            name='image',
            field=models.ImageField(verbose_name='回报图片', null=True, upload_to='return/%Y/%m'),
        ),
    ]
