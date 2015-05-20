# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email l911911951@alunos.ipbeja.pt
"""

from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect

from iot.models import Sensor, ReadData


#from forms import AddEquipmentForm, FichaEquipmentForm
#from iot.models import Equipment, PhysicalCharacteristic, Voltage, Memory
def listSensors(request):
    """
    Lista todos os sensores de um equipamento registrado
    """
    
    TITULO = _(u'Equipamentos')

    sensores = Sensor.objects.all().order_by('name')
    tamLista = len(sensores)
    template = "sensor/index.html"
    return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request)
                              )


#@csrf_exempt
def sensor(request, *args, **kwargs):
    
    idSensor = kwargs["idSensor"]
    
    sensor = Sensor.objects.get(id = idSensor)
    
    if request.method == 'GET':
        
        sensorData = ReadData.objects.latest('id')
        print'SENSOR DATA', 
        temp = int(sensorData.temperature)
        hum = int(sensorData.humidity)
        
        
        template = "sensorData/index.html"
        return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request)
                              )
    #===========================================================================
    # template = "sensor/index.html"
    # return render_to_response(template,
    #                           locals(),
    #                           context_instance=RequestContext(request))
    #===========================================================================

