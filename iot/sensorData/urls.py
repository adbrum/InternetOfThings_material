# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email: l911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, url
from iot import *


urlpatterns = patterns('',
                       url(r'^save/$', 'iot.sensorData.views.saveData', name="saveData"),
                       url(r'^load/(?P<idSensor>\d+)/$', 'iot.sensorData.views.loadData', name="loadData"),
                       
                       #^r/(?P<content_type_id>\d+)/(?P<object_id>.+)/$ [name='view_on_site']
                       )

