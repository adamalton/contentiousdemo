from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'contentioussite.views.index', name='index'),

    url(r'^data/', include('contentious.contrib.common.urls')),


)
