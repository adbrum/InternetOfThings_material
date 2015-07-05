# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
:Autor: Adriano Leal
:Aluno: 11951
:email: 911911951@alunos.ipbeja.pt
"""
from audit_log.models.fields import CreatingUserField, LastUserField
from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import FloatField, IntegerField
from django.forms.widgets import PasswordInput
from django.utils.translation import ugettext_lazy as _
import netifaces
import os

from internet_of_things.settings import MEDIA_ROOT, STATIC_ROOT


class Microcomputer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    model = models.CharField(max_length=100, verbose_name='Modelo')
    processor = models.ForeignKey('Processor', blank=True, null=True, verbose_name='Processador')
    microcontroller = models.ForeignKey('Microcontroller', blank=True, null=True, verbose_name='Microcontrolador')
    GPU = models.ForeignKey('GPU', blank=True, null=True)
    operatingSystems = models.ForeignKey('OperatingSystem', blank=True, null=True, verbose_name='Sistema Operativo')
    dateManufacture = models.DateField(verbose_name='Data de Fabrico')
    userCreation = CreatingUserField(related_name="created_microcomputer")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.model
    
    class Meta:
        verbose_name = 'Microcomputador'
        verbose_name_plural = 'Microcomputadores'


class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    serialNumber = models.CharField(max_length=100, verbose_name='Número de Série')
    model = models.CharField(max_length=100, null=True, verbose_name='Modelo')
    function = models.CharField(max_length=100, null=True, verbose_name='Função')
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensores'
  

class PhysicalCharacteristic(models.Model):
    microComputer = models.ForeignKey('Microcomputer', verbose_name='Microcomputador')
    length = models.FloatField(default=0, verbose_name='Comprimento (mm)')
    width = models.FloatField(default=0, verbose_name='Largura (mm)')
    weight = models.FloatField(default=0, verbose_name='Peso (g)')
    
    def __unicode__(self):
        return self.microComputer.model
    
    class Meta:
        verbose_name = 'Característica Física'
        verbose_name_plural = 'Características Físicas'


class GPU(models.Model):
    type = models.CharField(max_length=100, verbose_name='Tipo')
    clockSpeed = models.IntegerField(verbose_name='Clock Speed MHz')
    userCreation = CreatingUserField(related_name="created_gpus")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.type
    
    class Meta:
        verbose_name = 'GPU'
        verbose_name_plural = 'GPUs'
 
 
class Processor(models.Model):
    type = models.CharField(max_length=100, verbose_name='Processador')
    clockSpeed = models.IntegerField(verbose_name='Clock Speed MHz')
    userCreation = CreatingUserField(related_name="created_processor")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)
    
    
    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name = 'Processador'
        verbose_name_plural = 'Processadores'


class Microcontroller(models.Model):
    type = models.CharField(max_length=100, verbose_name='Microcontrolador')
    clockSpeed = models.IntegerField(verbose_name='Clock Speed MHz')
    userCreation = CreatingUserField(related_name="created_microcontroller")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.type
    
    class Meta:
        verbose_name = 'Microcontrolador'
        verbose_name_plural = 'Microcontroladores'


class Interface(models.Model):
    microComputer = models.ForeignKey('Microcomputer', verbose_name='Microcomputador')
    hdmi = models.CharField(blank=True, max_length=100)
    USBPorts = models.CharField(blank=True, max_length=100, verbose_name='Porta USB')
    videoInput = models.CharField(blank=True, max_length=100, verbose_name='Entrada de vídeo')
    videoOutputs = models.CharField(blank=True, max_length=100, verbose_name='Saida de vídeo')
    audioInputs = models.CharField(blank=True, max_length=100, verbose_name='Entrada de audio')
    audioOutputs = models.CharField(blank=True, max_length=100, verbose_name='Saida de audio')
    storage = models.CharField(blank=True, max_length=100, verbose_name='Armazenamento')
    network = models.CharField(blank=True, max_length=100, verbose_name='Rede')
    wifi = models.CharField(blank=True, max_length=100, verbose_name='WiFi')
    jack = models.CharField(blank=True, max_length=100)
    GPIO = models.CharField(blank=True, max_length=100)
    digitalIOPins = models.IntegerField(default=0, verbose_name='Pinos I/O digital')
    analogInputPins = models.IntegerField(default=0, verbose_name='Pinos de entrada analógica')
    
    def __unicode__(self):
        return self.microComputer.model
    
    class Meta:
        verbose_name = 'Interface'
        verbose_name_plural = 'Interfaces'
        

class OperatingSystem(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    version = models.CharField(blank=True, max_length=100, verbose_name='Versão')
    userCreation = CreatingUserField(related_name="created_operationsystems")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Sistema Operativo'
        verbose_name_plural = 'Sistemas Operativos'


class Expansion(models.Model):
    type = models.CharField(max_length=100, verbose_name='Tipo')
    peripherals = models.CharField(blank=True, max_length=100, verbose_name='Periféricos')
    userCreation = CreatingUserField(related_name="created_expansions")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.type
    
    class Meta:
        verbose_name = 'Expansão'
        verbose_name_plural = 'Expansões'


class Accessory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    type = models.CharField(blank=True, max_length=100, verbose_name='Tipo')
    userCreation = CreatingUserField(related_name="created_accessory")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Acessório'
        verbose_name_plural = 'Acessórios'


class Memory(models.Model):
    microComputer = models.ForeignKey('Microcomputer', verbose_name='Microcomputador')
    
    KILOBYTE = 'KB'
    MEGABYTE = 'MB'
    GIGABYTE = 'GB'
    MEMORIA = (
        (KILOBYTE, 'KB'),
        (MEGABYTE, 'MB'),
        (GIGABYTE, 'GB')
        
    )
    
    RAM = models.FloatField(default=0, verbose_name='RAM')
    quantidadeRAM = models.CharField(null=False, max_length=2, verbose_name='Quantidade em',
                                      choices=MEMORIA,
                                      default=KILOBYTE)
    
    SRAM = models.FloatField(default=0, verbose_name='SRAM KB')
    EEPROM = models.FloatField(default=0, verbose_name='EEPROM KB')
    
    flashMemory = models.FloatField(default=0, verbose_name='Memória Flash')
    quantidadeFlashMemory = models.CharField(null=False, max_length=2, verbose_name='Quantidade em',
                                      choices=MEMORIA,
                                      default=KILOBYTE)
    
    def __unicode__(self):
        return self.microComputer.model
    
    class Meta: 
        verbose_name = 'Memória'
        verbose_name_plural = 'Memórias'
    

class Voltage(models.Model):
    microComputer = models.ForeignKey('Microcomputer', verbose_name='Microcomputador')
    operatingVoltage = models.FloatField(default=0, verbose_name='Voltagem Operacional (V)')
    inputVoltageRecommended = models.CharField(max_length=10, default=0, verbose_name='Voltagem recomendada (V)')
    IOCurrentMax = models.CharField(max_length=10, default=0, verbose_name='I/O Corrente limites (V)')
    DCCurrentperIOPin = models.IntegerField(default=0, verbose_name='DC Corrente por pino (mA)')
    DCCurrentfor3_3VPin = models.IntegerField(default=0, verbose_name='DC Corrente por 3.3 pino (mA)')
    powerRatings = models.CharField(blank=True, max_length=100, verbose_name='Classificações de energia')
    powerSource = models.CharField(blank=True, max_length=100, verbose_name='Fonte de energia')
    
    def __unicode__(self):
        return self.microComputer.model
    
    class Meta:
        verbose_name = 'Voltagem'
        verbose_name_plural = 'Voltagens'
    

class Equipment(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    model = models.CharField(blank=True, max_length=100, verbose_name='Modelo')
    microComputer = models.ForeignKey('Microcomputer', verbose_name='Microcomputador')
    serialNumber = models.CharField(max_length=100, verbose_name='Número de Série')
    sensor = models.ManyToManyField('Sensor', blank=True, verbose_name='Sensor')
    expansion = models.ManyToManyField('Expansion', blank=True, verbose_name='Expansão')
    accessory = models.ManyToManyField('Accessory', blank=True, verbose_name='Acessório')
    userCreation = CreatingUserField(related_name="created_equipments")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

    
class RelativePosition(models.Model):
    nameElement = models.CharField(max_length=100)
    leftX = models.FloatField(default=0.0)
    topY = models.FloatField(default=0.0)
    width = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)
    
class Template(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome do Template')
    imagePath = models.FileField(upload_to="static/img", blank=True)
    equipment = models.ManyToManyField('Equipment', verbose_name='Equipamentos')
    
    def __unicode__(self):
        return self.name
    
    
class ReadData(models.Model):
    sensorId = models.IntegerField()
    temperature = FloatField(verbose_name='Temperatura')
    humidity = FloatField(verbose_name='Humidade')
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    
class Parameter(models.Model):
    equipment = models.ForeignKey('Equipment', verbose_name='Equipamentos')
    ip = models.CharField(max_length=100, verbose_name='Endereço IP')
    userName = models.CharField(max_length=100, verbose_name='Utilizador')
    password = models.CharField(max_length=100, verbose_name='Palavra passe')
    confirm_password = models.CharField(max_length=200, verbose_name='Confirme a palavra passe')
    sensorId = models.IntegerField(verbose_name='ID do sensor')
    timeRead = models.IntegerField(verbose_name='Tempo do ciclo de leitura')
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    
    def save(self,  *args, **kwargs):
        """
        Salva os parametros necessários para a comunicação cliente servidor.
        Copia o ficheiro com os parametros para o cliente.    
        """
        data = open(STATIC_ROOT+'dados.txt', 'w')

        localhost = netifaces.ifaddresses('eth0')[2][0]['addr']
        data.write(str(localhost)+'\n')
        data.write(str(self.sensorId)+'\n')
        data.write(str(self.timeRead)+'\n')

        data.close()

        #realiza a copia do ficheiro com os parâmetros de leitura
        os.system("sudo sshpass -p "+self.password+" rsync -av --progress "+STATIC_ROOT+"dados.txt "+self.userName+"@"+self.ip+":/home/"+self.userName+"/swms/")
        super(Parameter, self).save(*args, **kwargs) # Call the "real" save() method.
       
    def __unicode__(self):
        return self.equipment.name
    
    class Meta:
        verbose_name = 'Parâmetro cliente'
        verbose_name_plural = 'Parâmetros cliente'
    
    
        
