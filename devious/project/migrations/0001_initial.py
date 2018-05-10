# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='项目名称', max_length=255)),
                ('desc', models.CharField(verbose_name='项目描述', max_length=255)),
                ('members', models.IntegerField(verbose_name='关注人数')),
                ('money', models.BigIntegerField(verbose_name='钱')),
                ('status', models.SmallIntegerField(choices=[(0, '即将开始'), (1, '众筹中'), (2, '众筹成功'), (3, '众筹失败')], verbose_name='项目状态', default=0)),
                ('createdate', models.DateField(verbose_name='创建项目的时间', auto_now=True)),
                ('follower', models.IntegerField(verbose_name='支持人数')),
            ],
            options={
                'verbose_name': '众筹项目',
                'verbose_name_plural': '众筹项目',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='类别名称', max_length=100)),
                ('project', models.ForeignKey(verbose_name='项目', to='project.Project')),
            ],
            options={
                'verbose_name': '项目类别',
                'verbose_name_plural': '项目类别',
            },
        ),
    ]
