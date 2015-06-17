# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email: 911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView


urlpatterns = patterns('',
                       url(r'^$', lambda x: HttpResponseRedirect('/admin/')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^home/', include('iot.home.urls')),
                       url(r'^sensor/', include('iot.sensor.urls')),
                       url(r'^equipments/', include('iot.equipment.urls')),
                       url(r'^sensorData/', include('iot.sensorData.urls')),
                       (r'^500/$', TemplateView.as_view(template_name="500.html")),
                       (r'^404/$', TemplateView.as_view(template_name="404.html")),
                       )