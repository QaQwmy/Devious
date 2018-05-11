# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.contrib.auth.models
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], unique=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(blank=True, verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(blank=True, verbose_name='last name', max_length=30)),
                ('email', models.EmailField(blank=True, verbose_name='email address', max_length=254)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('authstatus', models.SmallIntegerField(default=0, choices=[(0, '未实名认证'), (1, '实名认证申请中'), (2, '已实名认证')], verbose_name='用户状态')),
                ('usertype', models.BooleanField(default=0, choices=[(0, '个人'), (1, '企业')], verbose_name='用户类型')),
                ('realname', models.CharField(verbose_name='真实姓名', max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', to='auth.Group', related_query_name='user', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions', to='auth.Permission', related_query_name='user', related_name='user_set')),
            ],
            options={
                'verbose_name_plural': '用户信息表',
                'verbose_name': '用户信息表',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='EmailCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(verbose_name='验证码', max_length=20)),
                ('email', models.EmailField(verbose_name='邮箱', max_length=20)),
                ('send_type', models.CharField(choices=[('register', '注册'), ('forgot', '忘记密码'), ('update_email', '修改邮箱')], verbose_name='验证码类型', max_length=40)),
                ('send_time', models.DateField(default=datetime.datetime.now, verbose_name='发送时间')),
            ],
            options={
                'verbose_name_plural': '邮箱验证码',
                'verbose_name': '邮箱验证码',
            },
        ),
    ]
