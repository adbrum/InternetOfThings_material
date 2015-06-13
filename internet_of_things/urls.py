# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email: 911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http.response import HttpResponseRedirect


urlpatterns = patterns('',
                       url(r'^$', lambda x: HttpResponseRedirect('/admin/')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^home/', include('iot.home.urls')),
                       url(r'^sensor/', include('iot.sensor.urls')),
                       url(r'^equipments/', include('iot.equipment.urls')),
                       url(r'^sensorData/', include('iot.sensorData.urls')),
                       )

handler404 = 'views.custom_404'
handler500 = 'views.custom_500'