from django.conf.urls import url
from users import views
urlpatterns = [
	# 首页
	url(r'^$',views.IndexView.as_view(),name='index'),
	# 登录
	url(r'^login/$',views.UserLoginView.as_view(),name='login'),
	# 注册
	url(r'^register/$',views.UserRegisterView.as_view(),name='register'),
	# 注册激活
	url(r'^active/(?P<active_code>.*)',views.ActiveUserView.as_view(),name='active'),
	# 退出
	url(r'^logout/$',views.UserLogoutView.as_view(),name='logout'),
]