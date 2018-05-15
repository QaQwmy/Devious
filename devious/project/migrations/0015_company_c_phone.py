# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_company_aut'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='c_phone',
            field=models.CharField(null=True, verbose_name='电话', max_length=20),
        ),
    ]
