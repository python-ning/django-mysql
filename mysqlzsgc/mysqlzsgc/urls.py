# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from zsgc.views import *
from zsgc.models import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'zsgc.views.index'),
    url(r'^add/$', 'zsgc.views.add', name='add'),
    url(r'^delete/$', 'zsgc.views.delete', name='delete'),
    url(r'^index$', 'zsgc.views.index', name='index'),
    url(r'^update/(\d+)/$', 'zsgc.views.update'),
    url(r'^delete/(\d+)$', 'zsgc.views.delete', name='delete')
]
