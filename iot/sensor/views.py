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
from iot.models import Sensor


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
    template = "sensor/index.html"
    return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request))

#===============================================================================
# 
# @csrf_protect
# def addEquipment(request):
#     """
#     Adiciona um equipamento novo
#     """
#     
#     TITULO = _(u'Equipamentos')
#     NOME_BREAD = _(u'Novo')
#     TITULO_BOTAO = _(u'Guardar')
# 
#     saveNew = True
# 
#     if request.method == 'POST':
#         form = AddEquipmentForm(request.POST)
# 
#         # Caso Click em cancelar
#         # Retorna para a listagem
#         if 'Cancelar' in request.POST or 'listEquipment' in request.POST:
#             return HttpResponseRedirect(reverse('listEquipment'))
# 
#         if form.is_valid():
# 
#             tableEquipament = Equipment(
#                 name=form.cleaned_data['name'],
#                 model=form.cleaned_data['model'],
#                 microComputer = form.cleaned_data['microComputer'],
#                 sensor = form.cleaned_data['sensor'],
#                 expansion = form.cleaned_data['expansion'],
#                 accessory = form.cleaned_data['accessory'],
#                 dateTimeCreation=datetime.now(),
#                 userCreation=request.user,
#                 dateTimeChange=datetime.now(),
#                 serAmendment=request.user,
#             )
#             
#             tableEquipament.save()
#             
#             if 'SaveAndNew' in request.POST:
#                 form = AddEquipmentForm()
#                 template = "equipment/add.html"
# 
#             else:
#                 return HttpResponseRedirect(reverse('listEquipment'))
# 
#         else:
#             template = "equipment/add.html"
# 
#     else:
#         # img =  "/static/img/placeholder.png"
#         form = AddEquipmentForm()
#         template = "equipment/add.html"
# 
#     return render_to_response(template,
#                               locals(),
#                               context_instance=RequestContext(request),
#                               )
#===============================================================================