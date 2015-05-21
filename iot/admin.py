from _functools import partial

from django.contrib import admin
from django.forms.widgets import MediaDefiningClass
from iot.models import Processor, Microcomputer, PhysicalCharacteristic, Voltage, \
GPU, OperatingSystem, Interface, Expansion, Accessory, Memory, Equipment, Sensor, Microcontroller, Template


class MicrocomputerAdmin(admin.ModelAdmin):
    list_display = ('model', 'name')
    search_fields = ['name']
    ordering = ('model',)
    

admin.site.register(Microcomputer, MicrocomputerAdmin)

class MicrocontrollerAdmin(admin.ModelAdmin):
    list_display = ('type', 'clockSpeed')
    search_fields = ['type']
    ordering = ('type',)
    

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name')
    search_fields = ['name']
    ordering = ('name',)

    
admin.site.register(Microcontroller, MicrocontrollerAdmin)
admin.site.register(Equipment)
admin.site.register(Processor)
admin.site.register(PhysicalCharacteristic)
admin.site.register(GPU)
admin.site.register(OperatingSystem)
admin.site.register(Interface)
admin.site.register(Expansion)
admin.site.register(Accessory)
admin.site.register(Memory)
admin.site.register(Sensor)
admin.site.register(Voltage)
admin.site.register(Template)


