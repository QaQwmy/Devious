from django.shortcuts import render
from django.views.generic import View
from project.models import Tag, Project
from pure_pagination import Paginator, PageNotAnInteger
from users.models import UserFlower,Address
from django.http import HttpResponse
import json
from project.models import Company
from users.models import UserProfile
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.


class ProjectListView(View):
	def get(self, request):
		current_page = 'overview'
		project_list = Project.objects.all()
		tags = Tag.objects.all()
		search_keywords = request.GET.get('keywords')
		print(search_keywords,'-------------------')
		if search_keywords:
			project_list = Project.objects.filter(
				Q(name__icontains=search_keywords)
			)
		sort = request.GET.get('sort', '')
		if sort:
			tag = Tag.objects.get(id=int(sort))
			project_list = tag.project_set.all()
		status = request.GET.get('status', '')

		if status:
			project_list = Project.objects.filter(status=int(status))
		sorts = request.GET.get('sorts', '')
		if sorts:
			if sorts == 0:
				project_list = Project.objects.all().order_by('')
			elif sorts == 1:
				project_list = Project.objects.all().order_by('-money')
			elif sorts == 2:
				project_list = Project.objects.all().order_by('-supporter')

		project_nums = project_list.count()
		try:
			page = request.GET.get('page', 1)
		except PageNotAnInteger:
			page = 1

		p = Paginator(project_list, 1, request=request)

		project_list = p.page(page)
		return render(request, 'project/projects.html', {'projects': project_list, 'current_page': current_page,
														 'project_nums': project_nums,
														 'tag_list': tags,
														 'sort': sort,
														 'status': status,
														 'sorts': sorts,
														 })


# 项目详情页
class ProjectDetailView(View):
	def get(self, request, p_id):
		pro = Project.objects.get(id=p_id)
		fav_com = False
		if pro:
			if UserFlower.objects.filter(user=request.user, company=pro.id):
				fav_com = True
			fav_user = UserFlower.objects.filter(company=pro.id)
			num = len([fav.user for fav in fav_user])
			return_goods = pro.returngoods_set.all()
			return render(request, 'project/project.html', {'project': pro, 'fav_com': fav_com, 'num': num,'return_goods':return_goods})


# 关注公司
class AddFavView(View):
	def post(self, request):
		project_id = request.POST.get('fav_id')
		company = Company.objects.get(id=project_id)
		res = dict()
		if not request.user.is_authenticated():
			res['status'] = 'fail'
			res['msg'] = '用户未登陆'
			return HttpResponse(json.dumps(res), content_type='application/json')
		fav = UserFlower.objects.filter(user=request.user, company=int(project_id))
		if fav:
			fav.delete()
			res['status'] = 'success'
			res['msg'] = '关注'
		else:
			if company:
				user_fav = UserFlower()
				user_fav.user = request.user
				user_fav.company = company
				user_fav.save()
				res['status'] = 'success'
				res['msg'] = '已关注'
			else:
				res['status'] = 'fail'
				res['msg'] = '关注失败'

		return HttpResponse(json.dumps(res), content_type='application/json')


class SupportView(View):
	def get(self, request):
		p_id = request.GET.get('id')
		mon = request.GET.get('mon')
		project = Project.objects.get(id=p_id)

		return render(request, 'project/pay-step-1.html', {
			'project': project,
			'money': mon,
		})


# 去结算
class GoPayView(View):
	def get(self, request):
		p_id = request.GET.get('id')
		mon = request.GET.get('mon')
		project = Project.objects.get(id=p_id)
		return render(request, 'project/pay-step-2.html',{
			'project': project,
			'money': mon,
		})


	def post(self,request):
			name = request.POST.get('name')
			phone = request.POST.get('phone')
			address1 = request.POST.get('address')
			address2 = Address()
			address2.name = name
			address2.user = request.user
			address2.phone = phone
			address2.address = address1
			address2.save()

			return JsonResponse({'res':1})


