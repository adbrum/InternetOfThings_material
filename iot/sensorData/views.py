# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email: l911911951@alunos.ipbeja.pt
"""

import json

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from iot.models import Equipment, Sensor, RelativePosition, Template, ReadData


#@login_required
@csrf_exempt
def saveData(request, *args, **kwargs):
    """
    Salva na base de dados informações sobre Temperatura e Humidade recebidas de um ficheiro python executado no Unirest.    
    """
    
    TITULO = _(u'Internet das Coisas')

    if request.method == 'POST':
        temperatura = request.POST['temperatura']
        humidade = request.POST['humidade']

        tableReadData = ReadData(temperature = temperatura,
                                 humidity = humidade,
                                 )
        tableReadData.save()
        return HttpResponse(json.dumps({'done':True}), content_type = "application/json")
    else:
        return HttpResponse(json.dumps({'done':False}), content_type = "application/json")
        

#@login_required
@csrf_exempt
def loadData(request, *args, **kwargs):
    """
    Salva na base de dados informações sobre Temperatura e Humidade recebidas de um ficheiro python executado no Unirest.    
    """
    
    TITULO = _(u'Internet das Coisas')

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
        
        