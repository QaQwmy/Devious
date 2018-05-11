from django.shortcuts import render, redirect
from django.views.generic import View
from users.forms import UserRegisterForm, UserLoginForm
from users.models import UserProfile, EmailCode, Banner
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from users.send_email import send_register_email
from project.models import Tag


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
					if user.is_staff == True and typess == 'user':
						return render(request, 'users/main.html')

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
		return render(request, 'index.html')


