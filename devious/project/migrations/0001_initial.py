# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='项目名称')),
                ('desc', models.CharField(max_length=255, verbose_name='项目描述')),
                ('follower', models.IntegerField(verbose_name='关注人数')),
                ('money', models.BigIntegerField(verbose_name='钱')),
                ('supportmoney', models.BigIntegerField(verbose_name='支持的金额')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='截止日期')),
                ('image', models.ImageField(max_length=200, upload_to='image/%Y/%m', verbose_name='项目图片')),
                ('status', models.SmallIntegerField(default=0, choices=[(0, '即将开始'), (1, '众筹中'), (2, '众筹成功'), (3, '众筹失败')], verbose_name='项目状态')),
                ('supporter', models.IntegerField(verbose_name='支持人数')),
                ('members', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='支持的人')),
            ],
            options={
                'verbose_name_plural': '众筹项目',
                'verbose_name': '众筹项目',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='类别名称')),
            ],
            options={
                'verbose_name_plural': '项目类别',
                'verbose_name': '项目类别',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='tag',
            field=models.ForeignKey(to='project.Tag', verbose_name='类别'),
        ),
    ]
