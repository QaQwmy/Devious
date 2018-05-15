# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20180512_0313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='标签名字', max_length=20)),
                ('super_label', models.ForeignKey(null=True, to='project.Label')),
            ],
        ),
        migrations.AlterModelOptions(
            name='returngoods',
            options={'verbose_name_plural': '回报', 'verbose_name': '回报'},
        ),
    ]
