from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from project.models import Project, Company


# Create your models here.


class UserProfile(AbstractUser):
	authstatus = models.SmallIntegerField(default=0, choices=((0, '未实名认证'), (1, '实名认证申请中'), (2, '已实名认证')),
										  verbose_name='用户状态', null=False)
	usertype = models.BooleanField(default=0, choices=((0, '个人'), (1, '企业')), verbose_name='用户类型', null=False)
	realname = models.CharField(max_length=255, verbose_name='真实姓名')

	class Meta:
		verbose_name = '用户信息表'
		verbose_name_plural = verbose_name


class EmailCode(models.Model):
	code = models.CharField(max_length=20, verbose_name='验证码')
	email = models.EmailField(verbose_name='邮箱', max_length=20)
	send_type = models.CharField(max_length=40,
								 choices=(('register', '注册'), ('forgot', '忘记密码'), ('update_email', '修改邮箱')),
								 verbose_name='验证码类型')
	send_time = models.DateField(default=datetime.now, verbose_name='发送时间')

	class Meta:
		verbose_name = '邮箱验证码'
		verbose_name_plural = verbose_name


class Banner(models.Model):
	project = models.ForeignKey(Project, null=True)
	name = models.CharField(max_length=20, verbose_name='轮播图')
	image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='图片路径')
	url = models.URLField(verbose_name='链接')

	class Meta:
		verbose_name = '轮播图'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


class UserSupprot(models.Model):
	user = models.ForeignKey(UserProfile, verbose_name='支持者')
	project = models.ForeignKey(Project, verbose_name='支持的项目')
	add_time = models.DateField(verbose_name='支持时间', default=datetime.now)

	class Meta:
		verbose_name = '用户支持'
		verbose_name_plural = verbose_name


class UserFlower(models.Model):
	user = models.ForeignKey(UserProfile, verbose_name='关注的人')
	company = models.ForeignKey(Project, verbose_name='关注的公司')
	add_time = models.DateField(verbose_name='关注的时间', default=datetime.now)

	class Meta:
		verbose_name = '用户关注'
		verbose_name_plural = verbose_name


class Address(models.Model):
	user = models.ForeignKey(UserProfile, verbose_name='用户')
	name = models.CharField(max_length=30, verbose_name='收货人', null=True)
	address = models.CharField(max_length=100, verbose_name='收货地址')
	phone = models.BigIntegerField(verbose_name='手机号码')

	class Meta:
		verbose_name = '收货地址'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.address


class UserCreate(models.Model):
	user = models.ForeignKey(UserProfile, verbose_name='创建项目的人')
	project = models.ForeignKey(Project, verbose_name='创建的项目')
	add_time = models.DateField(verbose_name='关注的时间', default=datetime.now)

	class Meta:
		verbose_name_plural = verbose_name = '创建项目表'

	def __str__(self):
		return self.user.username
