# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email: 911911951@alunos.ipbeja.pt
"""

from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect

from iot import equipment
from iot.models import Sensor, Equipment


def listEquipment_sensor(request, *args, **kwargs):
    """
    Realiza uma consulta na base de dados retornando uma lista de equipamentos registados.
    """
    
    idTemplate = kwargs['idEquipment']

    equipamentos = Equipment.objects.filter(id = idTemplate)
   
    response_data = []
    try:
        for equipamento in equipamentos:
            
            dictEquip =  {"equipamento_id":equipamento.id,
                          "nomeEquipamento":equipamento.name}
            lSensor = []
            for sensor in equipamento.sensor.all():
                s = Sensor.objects.get(id=sensor.id)
                dictSensor =  {"sensor_id":s.id,
                               "nome_sensor":s.name}
                lSensor.append(dictSensor)
                
            dictEquip["sensores"] = lSensor
            response_data.append(dictEquip)
    except:
        pass    
    
    template = "equipment/index.html"
    return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request)
                              )