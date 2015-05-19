# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email l911911951@alunos.ipbeja.pt
"""
from django import forms
from django.utils.translation import ugettext_lazy as _
# Class para editar um tipo documento
from iot.models import Equipment, MicroComputer, Sensor, Expansion, Accessory


class FichaEquipmentForm(forms.Form):

    name = forms.CharField(max_length=50, \
                           label=_(u'Nome'), \
                           widget=forms.TextInput(attrs={'class':'form-control vTextField required_form', 'autofocus':"autofocus", 'disabled':"disabled"}))
    
    model = forms.CharField(max_length=30, \
                                label=_(u'Modelo'), \
                                widget=forms.TextInput(attrs={'class':'form-control vTextField required_form', 'disabled':"disabled"}))
    
    microComputer = forms.ModelChoiceField(MicroComputer.objects.all(), \
                                     label = _(u'Micro Computador'), \
                                     widget = forms.Select(attrs = {'class':'form-control vTextField required_form', 'disabled':"disabled"})
                                     )
    
    sensor = forms.ModelChoiceField(Sensor.objects.all(), \
                                     label = _(u'Sensor'), \
                                     widget = forms.Select(attrs = {'class':'form-control vTextField required_form', 'disabled':"disabled"})
                                     )
    
    expansion = forms.ModelChoiceField(Sensor.objects.all(), \
                                     label = _(u'Expansão'), \
                                     widget = forms.Select(attrs = {'class':'form-control vTextField required_form', 'disabled':"disabled"})
                                     )
    
    accessory = forms.ModelChoiceField(Sensor.objects.all(), \
                                     label = _(u'Acessório'), \
                                     widget = forms.Select(attrs = {'class':'form-control vTextField required_form', 'disabled':"disabled"})
                                     )
    

class AddEquipmentForm(forms.Form):
    
    name = forms.CharField(max_length=100, \
                           label=_(u'Nome'), \
                           widget=forms.TextInput(attrs={'class':'form-control vTextField required_form', 'autofocus':"autofocus"}))

    model = forms.CharField(max_length=30, \
                                label=_(u'Modelo'), \
                                widget=forms.TextInput(attrs={'class':'form-control vTextField required_form'}))
    
    microComputer = forms.ModelChoiceField(MicroComputer.objects.all(), \
                                     label = _(u'Micro Computador'), \
                                     widget = forms.Select(attrs = {'class':'form-control vTextField required_form'})
                                     )
    
    sensor = forms.ModelChoiceField(Sensor.objects.all(), \
                                     label = _(u'Sensor'), \
                                     widget = forms.Select(attrs = {'class':'form-control vTextField required_form'})
                                     )
    
    expansion = forms.ModelChoiceField(Expansion.objects.all(), \
                                     label = _(u'Expansão'), \
                                     widget = forms.Select(attrs = {'class':'form-control vTextField required_form'})
                                     )
    
    accessory = forms.ModelChoiceField(Accessory.objects.all(), \
                                     label = _(u'Acessório'), \
                                     widget = forms.Select(attrs = {'class':'form-control vTextField required_form'})
                                     )

    class Meta:
        model = Equipment 
        fields = []
