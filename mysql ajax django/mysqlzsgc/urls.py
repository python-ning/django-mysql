# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from zsgc.views import *
from zsgc.models import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # 基于hellword的绑定
    url(r'^$', 'zsgc.views.index'),
    url(r'^add/$', 'zsgc.views.control', name='add'),
    url(r'^delete/$', 'zsgc.views.delete', name='delete'),
]
