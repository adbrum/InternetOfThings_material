# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email: 911911951@alunos.ipbeja.pt
"""

from django import forms 
from django.db import models
from django.forms.models import ModelForm
from django.forms.widgets import PasswordInput

from iot.models import Parameter


class ParameterForm(ModelForm):
    
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and password != confirm_password:
            raise forms.ValidationError("A confirmação da palavra passe não confere!")
    
        return self.cleaned_data
    
    class Meta:
        model = Parameter
        widgets = {
            'password': PasswordInput(),
            'confirm_password': PasswordInput(),
        }


