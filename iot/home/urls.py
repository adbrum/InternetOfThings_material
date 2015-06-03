# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email l911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, url
from iot import *


urlpatterns = patterns('',
                       url(r'^$', 'iot.home.views.index', name="home"),
                       url(r'^equipamentos/(?P<idTemplate>\d+)/$', 'iot.home.views.equipamentos', name="equipamentos"),
                       url(r'^getPosition', 'iot.home.views.getEquipmentPosition', name="getEquipmentPosition"),
                       url(r'^addPosition', 'iot.home.views.addEquipmentPosition', name="addEquipmentPosition"),
                       url(r'^getTemplate', 'iot.home.views.getTemplate', name="getTemplate"),
                       )

