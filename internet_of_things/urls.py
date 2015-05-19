# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email: l911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
                       #url(r'^', include('iot.login.urls')),
                       url(r'^$', include('iot.home.urls')),
                       url(r'^login/$', 'django.contrib.auth.views.login'),
                       url(r'^baseDados/', include('iot.baseDados.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       #url(r'^login/', include('iot.login.urls')),
                       url(r'^home/', include('iot.home.urls')),
                       url(r'^sensor/', include('iot.sensor.urls')),
                       url(r'^equipments/', include('iot.equipment.urls')),
                       #========================================================
                       # url(r'^equipments/', include('iot.equipment.urls')),
                       # url(r'^processors/', include('iot.processor.urls')),
                       # url(r'^microComputers/', include('iot.microComputer.urls')),
                       # url(r'^sensors/', include('iot.sensor.urls')),
                       # url(r'^gpus/', include('iot.gpu.urls')),
                       # url(r'^interfaces/', include('iot.interface.urls')),
                       # url(r'^operatingSystems/', include('iot.operatingSystem.urls')),
                       # url(r'^expansions/', include('iot.expansion.urls')),
                       # url(r'^accessories/', include('iot.accessory.urls')),
                       # url(r'^memories/', include('iot.memory.urls')),
                       #========================================================
                       
                       )
