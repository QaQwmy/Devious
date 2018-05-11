from django.conf.urls import url
from project import views


urlpatterns = [
	url(r'^list/$',views.ProjectListView.as_view(),name='list'),
	url(r'^detail/(?P<p_id>.*)',views.ProjectDetailView.as_view(),name='detail'),
	url(r'^fav/$',views.AddFavView.as_view(),name='fav'),
	url(r'^pay/$',views.SupportView.as_view(),name='pay'),
	url(r'^gopay/$',views.GoPayView.as_view(),name='go_pay'),

]