from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.


class UserProfile(AbstractUser):
	authstatus = models.SmallIntegerField(default=0,choices=((0,'未实名认证'),(1,'实名认证申请中'),(2,'已实名认证')),verbose_name='用户状态',null=False)
	usertype = models.BooleanField(default=0,choices=((0,'个人'),(1,'企业')),verbose_name='用户类型',null=False)
	realname = models.CharField(max_length=255,verbose_name='真实姓名')

	class Meta:

		verbose_name = '用户信息表'
		verbose_name_plural = verbose_name


class EmailCode(models.Model):
	code = models.CharField(max_length=20,verbose_name='验证码')
	email = models.EmailField(verbose_name='邮箱',max_length=20)
	send_type = models.CharField(max_length=40,choices=(('register','注册'),('forgot','忘记密码'),('update_email','修改邮箱')),verbose_name='验证码类型')
	send_time = models.DateField(default=datetime.now,verbose_name='发送时间')

	class Meta:
		verbose_name = '邮箱验证码'
		verbose_name_plural = verbose_name