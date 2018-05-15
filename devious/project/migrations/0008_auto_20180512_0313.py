# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_project_returns'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('types', models.CharField(max_length=100, choices=[(0, '无发票'), (1, '个人发票'), (2, '自定义发票')])),
            ],
        ),
        migrations.CreateModel(
            name='ReturnGoods',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('pay_money', models.BigIntegerField(verbose_name='支付金额')),
                ('palces', models.CharField(max_length=10, default='无限制', verbose_name='名额')),
                ('limit_purch', models.CharField(max_length=20, default='不限购', verbose_name='单笔限购')),
                ('return_goods_time', models.IntegerField(verbose_name='回报时间')),
                ('freight', models.IntegerField(default=0, verbose_name='运费')),
                ('invoice', models.ForeignKey(to='project.Invoice', verbose_name='发票')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='time',
            field=models.IntegerField(null=True, verbose_name='筹集时间'),
        ),
        migrations.AddField(
            model_name='returngoods',
            name='project',
            field=models.ForeignKey(to='project.Project', verbose_name='项目名称'),
        ),
    ]
