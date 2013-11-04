from django.conf.urls import patterns, include, url
from player import views

urlpatterns = patterns('',
  url(r'^all/$', views.all),
  url(r'^top-100/$', views.top_100),
  url(r'^qb/$', views.qb),
)