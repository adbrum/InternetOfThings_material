# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email: 911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, url

from iot import *


urlpatterns = patterns('',
                       url(r'^save/$', 'iot.sensorData.views.saveData', name="saveData"),
                       url(r'^load/(?P<idSensor>\d+)/$', 'iot.sensorData.views.loadData', name="loadData"),
                       url(r'^configParameters/', 'iot.sensorData.views.configParameters', name="configParameters"),
                       )

