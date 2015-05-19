# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email l911911951@alunos.ipbeja.pt
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
    Página principal do utilizador
    """
    
    TITULO = _(u'Internet das Coisas')
  
    template = "home/index.html"
    return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request)
                              )

#@login_required
@csrf_exempt
def equipamentos(request, *args, **kwargs):
    """
    Lista todos os equipamentos com os seus sensores que foram inseridos no sistema
    """
    
    idTemplate = kwargs['idTemplate']

    TITULO = _(u'Internet das Coisas')
    
    template = Template.objects.filter(id = idTemplate).order_by('name')
    for i in template:
        for j in i.equipment.all():
            print'EQUIPAMENTO: ', i.id

            equipamentos = Equipment.objects.filter(id = i.id).order_by('name')
            
            for i in equipamentos:
                print'TEMPLATE: ', i.name
            
            
            #===========================================================================
            # response_data = [{"equipamento_id":1, "nomeEquipamento":"EquipSEI_LA", "sensores":[{"sensor_id":2, "nome_sensor":"OLA"}]},
            #  {"equipamento_id":2, "nomeEquipamento":"EquipSEI_LA", "sensores":[{"sensor_id":2, "nome_sensor":"OLA"}]},
            #  {"equipamento_id":3, "nomeEquipamento":"EquipSEI_LA", "sensores":[{"sensor_id":2, "nome_sensor":"OLA"}]}
            #  ]
            #===========================================================================
            
            
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
                    print s.name
                    '''
                    response_data.append(
                                   {"equipamento_id":equipamento.id,
                                     "nomeEquipamento":equipamento.name,
                                     "sensores":[{"sensor_id":s.id,
                                                  "nome_sensor":s.name}]
                                    })
                    '''
                    
                dictEquip["sensores"] = lSensor
                response_data.append(dictEquip)
        
        
    print json.dumps(response_data)
    
    #return HttpResponse(retorno, mimetype="text/javascript")
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
    print "AQUI", dados
    for equipamento, valores in dados.iteritems():
        print "EQUIPAMENTO ", equipamento, "VALORES", valores
        dict = {"topY": valores["y"], "leftX":valores["x"]}
          
        posicaoTable = RelativePosition.objects.update_or_create(nameElement = equipamento,
                                        defaults=dict
                                        )
    
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
            print 'TEMPLATE: ',item.name
            response_data.append({"id":item.id,
                                  "nome":item.name,
                                  "caminhoImagem":str(item.imagePath)})
    
    return HttpResponse(json.dumps(response_data), content_type = "application/json")


