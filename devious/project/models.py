from django.db import models
from datetime import datetime

# Create your models here.


class Tag(models.Model):
	name = models.CharField(max_length=100,verbose_name='类别名称')



	class Meta:
		verbose_name = '项目类别'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


class Project(models.Model):
	name = models.CharField(max_length=255,verbose_name='项目名称')
	desc = models.CharField(max_length=255,verbose_name='项目描述')
	follower = models.IntegerField(verbose_name='关注人数')
	money = models.BigIntegerField(verbose_name='钱')
	supportmoney = models.BigIntegerField(verbose_name='支持的金额')
	date = models.DateField(verbose_name='截止日期',default=datetime.now)
	image1 = models.ImageField(max_length=200,upload_to='image/%Y/%m',verbose_name='项目图片1',null=True)
	image2 = models.ImageField(max_length=200,upload_to='image/%Y/%m',verbose_name='项目图片2',null=True)
	status = models.SmallIntegerField(default=0,choices=((0,'即将开始'),(1,'众筹中'),(2,'众筹成功'),(3,'众筹失败')),verbose_name='项目状态')
	createdate = models.DateField(verbose_name='创建项目的时间',default=datetime.now)
	supporter = models.IntegerField(verbose_name='支持人数')
	tag = models.ForeignKey(Tag,verbose_name='类别')
	company = models.ForeignKey('Company',null=True)
	returns = models.CharField(max_length=255,verbose_name='回报内容',null=True)
	class Meta:
		verbose_name = '众筹项目'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


class Company(models.Model):
	name = models.CharField(max_length=60,verbose_name='公司名称')
	desc = models.CharField(max_length=255,verbose_name='公司简介')
	phone = models.IntegerField(verbose_name='客服电话')
	image = models.ImageField(upload_to='company/%Y/%m',null=True,verbose_name='公司图片')

	class Meta:
		verbose_name = '公司名称'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name