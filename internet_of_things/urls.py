# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email: l911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', include('iot.home.urls')),
                       #url(r'^login/$', 'django.contrib.auth.views.login'),
                       #url(r'^baseDados/', include('iot.baseDados.urls')),
                       #url(r'^login/', include('iot.login.urls')),
                       url(r'^home/', include('iot.home.urls')),
                       url(r'^sensor/', include('iot.sensor.urls')),
                       url(r'^equipments/', include('iot.equipment.urls')),
                       url(r'^sensorData/', include('iot.sensorData.urls')),
                       )
