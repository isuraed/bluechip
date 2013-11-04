from django.conf.urls import patterns, include, url
from player.views import bootstrap

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', bootstrap),
	url(r'^player/', include('player.urls')),
    # Examples:
    # url(r'^$', 'bluechip.views.home', name='home'),
    # url(r'^bluechip/', include('bluechip.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
