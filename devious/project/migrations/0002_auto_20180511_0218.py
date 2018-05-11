# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, verbose_name='公司名称')),
                ('desc', models.CharField(max_length=255, verbose_name='公司简介')),
                ('phone', models.IntegerField(verbose_name='客服电话')),
            ],
            options={
                'verbose_name_plural': '公司名称',
                'verbose_name': '公司名称',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='company',
            field=models.ForeignKey(null=True, to='project.Company'),
        ),
    ]
