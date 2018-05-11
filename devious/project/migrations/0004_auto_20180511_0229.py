# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_company_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AddField(
            model_name='project',
            name='image1',
            field=models.ImageField(upload_to='image/%Y/%m', null=True, verbose_name='项目图片1', max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='image2',
            field=models.ImageField(upload_to='image/%Y/%m', null=True, verbose_name='项目图片2', max_length=200),
        ),
    ]
