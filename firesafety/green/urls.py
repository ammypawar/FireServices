from django.conf.urls import patterns, url
from green import views

urlpatterns = patterns('',
	url(r'^$',views.demo,name='demo'),
	url(r'^contact_us/$', views.contact_us, name='contact_us'),
	)