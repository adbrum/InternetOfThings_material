from _functools import partial
from django.contrib import admin
from django.forms.widgets import MediaDefiningClass

from iot.models import Processor, Microcomputer, PhysicalCharacteristic, Voltage, \
GPU, OperatingSystem, Interface, Expansion, Accessory, Memory, Equipment, Sensor, Microcontroller, Template


class ModelAdminWithForeignKeyLinksMetaclass(MediaDefiningClass):

    def __getattr__(cls, name):

        def foreign_key_link(instance, field):
            target = getattr(instance, field)
            print u'<a href="../../%s/%s/%d">%s</a>' % (
                target._meta.app_label, target._meta.module_name, target.id, unicode(target))
            return u'<a href="../../%s/%s/%d">%s</a>' % (
                target._meta.app_label, target._meta.module_name, target.id, unicode(target))

        if name[:8] == 'link_to_':
            method = partial(foreign_key_link, field=name[8:])
            method.__name__ = name[8:]
            method.allow_tags = True
            setattr(cls, name, method)
            return getattr(cls, name)
        raise AttributeError


class MicrocomputerAdmin(admin.ModelAdmin):
    list_display = ('model', 'name')
    ordering = ('model',)
    

admin.site.register(Microcomputer, MicrocomputerAdmin)

class MicrocontrollerAdmin(admin.ModelAdmin):
    list_display = ('type', 'clockSpeed')
    ordering = ('type',)
    

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name')
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

