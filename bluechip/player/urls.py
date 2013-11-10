from django.conf.urls import patterns, include, url
from player import views

urlpatterns = patterns('',
	url(r'^$', views.home),
	url(r'^all/$', views.all),
  	url(r'^top-100/$', views.top_100),
  	url(r'^by-position/([^/]+)/$', views.by_position),
  	url(r'^player-(\d+)/$', views.profile),
 )