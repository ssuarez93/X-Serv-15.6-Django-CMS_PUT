from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages', 'cms_put.views.lista_paginas'),
    url(r'^(\d+)', 'cms_put.views.identificador'),
    url(r'^(.*)$', 'cms_put.views.recurso')
)
