from django.db import models
from datetime import datetime


# Create your models here.


class Tag(models.Model):
	name = models.CharField(max_length=100, verbose_name='类别名称')

	class Meta:
		verbose_name = '项目类别'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


class Project(models.Model):
	name = models.CharField(max_length=255, verbose_name='项目名称')
	desc = models.CharField(max_length=255, verbose_name='项目描述')
	follower = models.IntegerField(verbose_name='关注人数', default=0)
	money = models.BigIntegerField(verbose_name='钱')
	supportmoney = models.BigIntegerField(verbose_name='支持的金额', null=True, default=0)
	time = models.IntegerField(verbose_name='筹集时间', null=True)
	date = models.DateField(verbose_name='截止日期')
	image1 = models.ImageField(max_length=200, upload_to='image/%Y/%m', verbose_name='项目图片1', null=True)
	image2 = models.ImageField(max_length=200, upload_to='image/%Y/%m', verbose_name='项目图片2', null=True)
	status = models.SmallIntegerField(default=0, choices=((0, '即将开始'), (1, '众筹中'), (2, '众筹成功'), (3, '众筹失败')),
									  verbose_name='项目状态')
	createdate = models.DateField(verbose_name='创建项目的时间', default=datetime.now)
	supporter = models.IntegerField(verbose_name='支持人数', null=True, default=0)
	tag = models.ForeignKey(Tag, verbose_name='类别')
	company = models.ForeignKey('Company', null=True)
	returns = models.CharField(max_length=255, verbose_name='回报内容', null=True)
	tags = models.CharField(max_length=100, verbose_name='项目标签', null=True)

	class Meta:
		verbose_name = '众筹项目'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name

	def get_time(self):
		endtime = self.date.strftime('%Y-%m_%d')
		endtime = datetime.strptime(endtime, '%Y-%m_%d')
		now = datetime.now().strftime('%Y-%m_%d')
		now = datetime.strptime(now, '%Y-%m_%d')

		left_time = (endtime - now).days
		if left_time > 0:
			self.status = 1
		elif left_time <= 0:
			if self.supportmoney >= self.money:
				self.status = 2
			else:
				self.status = 3
		return left_time


# 公司
class Company(models.Model):
	name = models.CharField(max_length=60, verbose_name='公司名称')
	desc = models.CharField(max_length=255, verbose_name='公司简介')
	c_phone = models.CharField(max_length=20, verbose_name='电话', null=True)
	phone = models.IntegerField(verbose_name='客服电话')
	image = models.ImageField(upload_to='company/%Y/%m', null=True, verbose_name='公司图片')
	aut = models.CharField(max_length=100, choices=((('0', '未认证'), ('1', '已认证'))), verbose_name='认证状态', default='0',
						   null=True)

	class Meta:
		verbose_name = '公司名称'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name

# 发票
class Invoice(models.Model):
	types = models.CharField(choices=(('0', '无发票'), ('1', '个人发票'), ('2', '自定义发票')), verbose_name='发票', max_length=20)

	def __str__(self):
		return 'Invoice'


class ReturnGoods(models.Model):
	project = models.ForeignKey(Project, verbose_name='项目名称')
	type = models.CharField(max_length=20, choices=(('0', '实物回报'), ('1', '虚拟物品回报')), verbose_name='回报类型', default='0')
	desc = models.CharField(max_length=100, verbose_name='回报简述', null=True)
	image = models.ImageField(upload_to='return/%Y/%m', verbose_name='回报图片', null=True)
	number = models.IntegerField(verbose_name='回报数量', null=True)
	pay_money = models.BigIntegerField(verbose_name='支付金额')
	palces = models.CharField(max_length=10, verbose_name='名额', default='无限制')
	limit_purch = models.CharField(max_length=20, verbose_name='单笔限购', default='不限购')
	return_goods_time = models.IntegerField(verbose_name='回报时间')
	freight = models.IntegerField(default=0, verbose_name='运费')
	invoice = models.CharField(max_length=20, choices=(('0', '无发票'), ('1', '个人发票'), ('2', '自定义发票')), verbose_name='发票')

	class Meta:
		verbose_name = '回报'
		verbose_name_plural = verbose_name

	def __str__(self):
		return 'aaa'


class Label(models.Model):
	name = models.CharField(max_length=20, verbose_name='标签名字')
	project = models.ForeignKey(Project, verbose_name='项目名称', null=True)

	class Meta:
		verbose_name = '标签'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name
