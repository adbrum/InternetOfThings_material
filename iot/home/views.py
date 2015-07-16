# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email: 911911951@alunos.ipbeja.pt
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
from iot.models import Equipment, Sensor, RelativePosition, Template


@login_required(login_url='/admin/login/')
def index(request):
    """
    Exibe a página principal de utilizador
    """

    template = "home/index.html"
    return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request)
                              )


@csrf_exempt
def equipamentos(request, *args, **kwargs):
    """
    Lista todos os equipamentos e sensores que foram inseridos no sistema
    """
    
    idTemplate = kwargs['idTemplate']

    template = Template.objects.filter(id = idTemplate).order_by('name')
    
    
    for i in template:
        
        
        for j in i.equipment.all():
            equipamentos = Equipment.objects.filter(id = j.id).order_by('name')

            response_data = []
            
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

    return HttpResponse(json.dumps(response_data), content_type = "application/json")


@csrf_exempt
def getEquipmentPosition(request):
    """
    Pega a posição de todos os equipamentos e sensores.
    """

    posicao = RelativePosition.objects.all()
   
    response_data = []
    
    for item in posicao:
        response_data.append({"nome":item.nameElement,
                              "X":item.leftX,
                              "Y":item.topY})

    return HttpResponse(json.dumps(response_data), content_type = "application/json")


@csrf_exempt
def addEquipmentPosition(request):
    """
    Salva a posição de todos os equipamentos e sensores.
    """
    #Recebe a string pelo POST e a transforma em objeto.
    dados = json.loads(request.POST.get('dados'))

    for equipamento, valores in dados.iteritems():
        dict = {"topY": valores["y"], "leftX":valores["x"]}
          
        posicaoTable, created = RelativePosition.objects.update_or_create(nameElement = equipamento,
                                        defaults=dict
                                        )
        if created:
            # means you have created a new person
            dict = {"topY": "180", "leftX":"278"}
        else:
            # person just refers to the existing one
            dict = {"topY": valores["y"], "leftX":valores["x"]}
    
    return HttpResponse(content_type = "application/json")



@csrf_exempt
def getTemplate(request, *args, **kwargs):
    """
    Pega os dados (Equipamentos e sensores) dos templates criados e envia para o template uma lista destes. 
    """
    
    idTemplate = request.POST.get("id_template")
    
    if idTemplate:
       
        template = Template.objects.get(id = idTemplate)
        response_data = {}
                                  
        response_data = {"id":template.id,
                              "nome":template.name,
                              "caminhoImagem":str(template.imagePath)}
    
    else:
 
        template = Template.objects.all().order_by('name')
        response_data = []
        
        for item in template:
            response_data.append({"id":item.id,
                                  "nome":item.name,
                                  "caminhoImagem":str(item.imagePath)})
    
    return HttpResponse(json.dumps(response_data), content_type = "application/json")


