from django.db import models

# Create your models here.


class Project(models.Model):
	name = models.CharField(max_length=255,verbose_name='项目名称')
	desc = models.CharField(max_length=255,verbose_name='项目描述')
	members = models.IntegerField(verbose_name='关注人数')
	money = models.BigIntegerField(verbose_name='钱')
	status = models.SmallIntegerField(default=0,choices=((0,'即将开始'),(1,'众筹中'),(2,'众筹成功'),(3,'众筹失败')),verbose_name='项目状态')
	createdate = models.DateField(verbose_name='创建项目的时间',auto_now=True)
	follower = models.IntegerField(verbose_name='支持人数')

	class Meta:
		verbose_name = '众筹项目'
		verbose_name_plural = verbose_name


class Tag(models.Model):
	name = models.CharField(max_length=100,verbose_name='类别名称')
	project = models.ForeignKey(Project,verbose_name='项目')


	class Meta:
		verbose_name = '项目类别'
		verbose_name_plural = verbose_name