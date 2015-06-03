# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email l911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^listSensors/$', 'iot.sensor.views.listSensors',
                           name="listSensors"),
                       url(r'^sensor/(?P<idSensor>\d+)/$', 'iot.sensor.views.sensor', name="sensor"),

                       )