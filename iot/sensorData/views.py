# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email: 911911951@alunos.ipbeja.pt
"""

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
import json
import netifaces
from os.path import os

from iot.models import Equipment, Sensor, RelativePosition, Template, ReadData


@csrf_exempt
def saveData(request, *args, **kwargs):
    """
    Salva na base de dados informações sobre Temperatura e Humidade, 
    estes dados são enviados por um script python executado no Raspberry Pi.    
    """

    if request.method == 'POST':
        sensor_id = request.POST['sensorId']
        temperatura = request.POST['temperatura']
        humidade = request.POST['humidade']
 
        tableReadData = ReadData(sensorId = sensor_id,
                                 temperature = temperatura,
                                 humidity = humidade
                                 )
        tableReadData.save()
        return HttpResponse(json.dumps({'done':True}), content_type = "application/json")
    else:
        return HttpResponse(json.dumps({'done':False}), content_type = "application/json")
        

@csrf_exempt
def loadData(request, *args, **kwargs):
    """
    Realiza uma persquisa na base de dados, retornando o último registo do sensor.    
    """
    
    idSensor = kwargs["idSensor"]

    if request.method == 'POST':
        
        response_data = []
        lastItem = []
         
        sensorData = ReadData.objects.filter(sensorId=idSensor)

        for sensorData in sensorData:
        
            lastItem.append({"sensorData_temp":int(sensorData.temperature),
                            "sensorData_hum":int(sensorData.humidity)})
        
        response_data.append(getattr(lastItem,  '__getitem__')(-1)) #This will return to you the last element as well    
        
        return HttpResponse(json.dumps(response_data), content_type = "application/json")

        
@csrf_exempt
def configParameters(request, *args, **kwargs):
    """
    Salva os parametros necessários para a comunicação cliente servidor.
    Copia o ficheiro com os parametros para o cliente.    
    """
    
    ipCopy =    kwargs["ip"]
    localhost = netifaces.ifaddresses('eth0')[2][0]['addr']
    idSensor =  kwargs["idSensor"]
    user =      kwargs["user"]
    password =  kwargs["password"]
    time =      kwargs["time"]

    if request.method == 'POST':
        
        data = open('dados.txt', 'w') 
        data.write(localhost)
        data.write(time)  
        
        data.close()
        
        #realiza a copia do ficheiro
        os.system("sshpass -p {0} rsync -av --progress {1} {2}@{3}:/home/adriano/Documentos/".format(password , '/home/adriano/Documentos/dados.txt',user ,ipCopy))
        
        template = "parameters/index.html"
        return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request)
                              )

                