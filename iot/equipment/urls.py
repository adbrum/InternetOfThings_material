# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email: 911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^listEquipment_sensor/(?P<idEquipment>\d+)/$', 'iot.equipment.views.listEquipment_sensor', name="listEquipment_sensor"),
                       )
