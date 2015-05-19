# -*- coding: utf-8 -*-
'''
Created on 27/04/2015

@author: adriano
'''
from django.apps import AppConfig
#from django.utils.translation import ugettext_lazy as _

'''Alterar nome da APP'''
class IOTConfig(AppConfig):
    name = 'iot'
    verbose_name = u'Administração'#_("Administration")