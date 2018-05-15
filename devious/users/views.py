import time
from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.views.generic import View
from users.forms import UserRegisterForm, UserLoginForm, AddressForm
from users.models import UserProfile, EmailCode, Banner, Address, UserCreate, UserSupprot, UserFlower
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from users.send_email import send_register_email
from project.models import Tag, Label, Company, Project
from django.http import JsonResponse
from django.core.files.storage import default_storage
from devious.settings import MEDIA_ROOT
from users.forms import Upload, Upload1
from project.models import ReturnGoods, Invoice, Label


# Create your views here.


# 首页
class IndexView(View):
	def get(self, request):
		banners = Banner.objects.all()
		tags = Tag.objects.all()
		return render(request, 'index.html', {'banners': banners, 'tags': tags})


# 用户登录
class UserLoginView(View):
	def get(self, request):
		return render(request, 'users/login.html')

	def post(self, request):
		login_form = UserLoginForm(request.POST)

		if login_form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')
			remember = request.POST.get('remember')
			typess = request.POST.get('typess')
			if typess == 'member':
				is_staff = 0
			else:
				is_staff = 1
			user = authenticate(username=username, password=password)
			print('aaaaa')
			if user is not None:
				if user.is_active:
					login(request, user)
					print('------------>', user.is_staff, typess)
					if user.is_staff == True:
						if typess == 'user':
							return redirect(reverse('admin'))
						else:
							return redirect(reverse('users:index'))

					elif user.is_staff == False and typess == 'member':
						return redirect(reverse('users:index'))
					else:
						return render(request, 'users/login.html', {'msg': '没有权限'})
				else:
					return render(request, 'users/login.html', {'msg': '用户未激活，请去激活'})
			else:
				return render(request, 'users/login.html', {'msg': '用户名或密码错误'})
		else:
			return render(request, 'users/login.html', {'login_form': login_form})


# 用户注册
class UserRegisterView(View):
	def get(self, request):
		return render(request, 'users/reg.html')

	def post(self, request):
		register_form = UserRegisterForm(request.POST)
		if register_form.is_valid():
			username = request.POST.get('username')
			email = request.POST.get('email')
			if UserProfile.objects.filter(username=username):
				return render(request, 'users/reg.html', {'msg': '用户名已存在', 'register_form': register_form})
			if UserProfile.objects.filter(email=email):
				return render(request, 'users/reg.html', {'msg': '邮箱已存在', 'register_form': register_form})
			password = request.POST.get('password')

			types = request.POST.get('type')
			print(types)
			user = UserProfile()
			user.username = username
			user.password = make_password(password=password)
			user.email = email
			user.usertype = types
			user.is_active = 0
			user.save()
			send_register_email(email, send_type='register')
			return render(request, 'users/login.html')
		return render(request, 'users/reg.html', {'register_form': register_form})


# 注册激活
class ActiveUserView(View):
	def get(self, request, active_code):
		records = EmailCode.objects.filter(code=active_code)
		if records:
			for record in records:
				email = record.email
				user = UserProfile.objects.get(email=email)
				user.is_active = 1
				user.save()
			return redirect(reverse('users:login'))
		return render(request, 'users/active_fail.html')


# 用户登出
class UserLogoutView(View):
	def get(self, request):
		user = request.user
		if user:
			logout(request)
			return redirect(reverse('users:index'))


# 发起众筹
class InitiateView(View):
	def get(self, request):
		return render(request, 'users/start.html')


# 发起众筹2
class Initiate2View(View):
	def get(self, request):
		tags = Tag.objects.all()
		labels = Label.objects.all()
		context = {
			'tags': tags,
			'labels': labels,
		}
		return render(request, 'users/start-step-1.html', context=context)




class Initiate6View(View):
	def get(self, request):
		return render(request, 'users/start-step-2.html')

	def post(self, request):
		tag = request.POST.get('tag')
		print(tag)
		label = request.POST.getlist('labelname')
		print(type(label))
		print(label)
		label_str = ','.join(label)
		p_name = request.POST.get('p_name')

		p_desc = request.POST.get('p_desc')
		p_money = request.POST.get('p_money')

		p_time = request.POST.get('p_time')
		image_title = save_image(str(int(time.time())) + request.FILES['image_title'].name, request.FILES['image_title'])
		image_detail = save_image(str(int(time.time())) + request.FILES['image_detail'].name, request.FILES['image_detail'])

		u_name = request.POST.get('u_name')
		u_phone = request.POST.get('u_phone')
		u_c_phone = request.POST.get("u_c_phone")
		u_desc = request.POST.get("u_desc")
		now = datetime.now()
		aDay = timedelta(days=30)
		now = now + aDay
		project = Project()
		project.name = p_name
		project.desc = p_desc
		print(p_money)
		project.money = int(p_money)
		project.image1 = image_title
		project.image2 = image_detail
		project.tags = label_str
		tags = Tag.objects.get(name=tag)
		project.tag = tags
		project.date = now.strftime('%Y-%m-%d')
		project.time = int(p_time)
		# project.status = '即将开始'
		project.save()
		company = Company()
		company.name = u_name
		company.desc = u_desc
		company.phone = u_c_phone
		company.c_phone = int(u_phone)
		company.aut = '未认证'

		company.save()
		projects = Project.objects.get(name=p_name)
		usercreate = UserCreate()
		usercreate.user = request.user
		usercreate.project = projects
		usercreate.save()
		return JsonResponse({"res": '1'})

class Initiate4View(View):
	def get(self, request):
		return render(request, 'users/start-step-3.html')


class Initiate5View(View):
	def get(self, request):
		return render(request, 'users/start-step-4.html')


# 会员中心
class UserInfo(View):
	def get(self, request):
		user = request.user
		if user:
			return render(request, 'users/member.html')


# 我的众筹
class MyDevious(View):
	def get(self, request):
		_user = request.user

		supp_p = UserSupprot.objects.filter(user=_user)
		flow_p = UserFlower.objects.filter(user=_user)
		cre_p = UserCreate.objects.filter(user=_user)
		return render(request, 'users/minecrowdfunding.html',
					  {'s_projects': supp_p, 'f_projects': flow_p, 'c_projects': cre_p})


# 实名认证
class RealName(View):
	def get(self, request):
		return render(request, 'users/accttype.html')


# 认证申请
class Apply_real(View):
	def get(self, request):
		return render(request, 'users/')


def save_image(image_detail_filename, file_obj):
	# 一定要有uploadimage文件夹
	with default_storage.open(MEDIA_ROOT + '/' + 'uploadimage' + '/' + image_detail_filename,'wb+') as file:
		for chunk in file_obj.chunks():
			file.write(chunk)
	image_detail_upload = 'uploadimage/' + image_detail_filename
	return image_detail_upload


class AddGoods(View):
	def post(self, request, pro_id):
		print('进4了')
		form = Upload1(request.POST, request.FILES)
		if form.is_valid():
			typeS = request.POST.get('type')
			money = request.POST.get('money')
			image = form.cleaned_data['image']
			desc = request.POST.get('desc')
			num = request.POST.get('number')
			limit = request.POST.get('limit')
			freight = request.POST.get('freight')
			invioce = request.POST.get('ok')
			timea = request.POST.get('time')
			rg = ReturnGoods()
			rg.desc = desc
			rg.image = image
			rg.freight = int(freight)
			rg.number = int(num)
			rg.limit_purch = limit
			rg.return_goods_time = int(timea)
			rg.type = typeS
			rg.pay_money = money

			rg.invoice = '自定义发票'
			project1 = Project.objects.get(id=int(pro_id))
			rg.project = project1
			rg.save()

			return render(request, 'users/start-step-2.html', {'project': project1})
