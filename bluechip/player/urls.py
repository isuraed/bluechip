from django.conf.urls import patterns, include, url
from player import views

urlpatterns = patterns('',
  url(r'^$', views.players),
)