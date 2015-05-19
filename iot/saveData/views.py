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
    Lista todos os equipamentos com os seus sensores que foram inseridos no sistema
    """
    
    temperatura = kwargs['temperatura']
    humidade = kwargs['humidade']
    
    print 'XXXXXXXXXXXXXXXXXXXXXXXXXX', temperatura, humidade
    

    TITULO = _(u'Internet das Coisas')
    
    tableReadData = ReadData(temperature = temperatura,
                             humidity = humidade,
                             )
    tableReadData.save()
    return render_to_response(context_instance=RequestContext(request) )
