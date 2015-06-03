# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email: l911911951@alunos.ipbeja.pt
"""

from django import template
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from iot.models import Equipment, PhysicalCharacteristic, Voltage, Memory, \
    Microcontroller, Microcomputer, GPU, Interface, Processor, Sensor, Template


def criar(request):
    """
    Cria ficheiros .json com os dados contidos na base de dados.
    """
    microcontrolador = Microcontroller.objects.filter()
     
    file_microcontroller = open("iot/fixtures/microcontroller.json", "w")
    file_microcontroller.write("[\n")
    qt = len(microcontrolador)
    for item in microcontrolador:
        file_microcontroller.write("\t{\n")
        file_microcontroller.write("\t\t\"model\": \"iot.Microcontroller\",\n")
        file_microcontroller.write("\t\t\"pk\": \"" + str(item.id) + "\",\n")
        file_microcontroller.write("\t\t\"fields\": {\n")
        file_microcontroller.write("\t\t\"type\" : \"" + (item.type).encode("utf-8\n") + "\",\n")
        file_microcontroller.write("\t\t\"clockSpeed\" : " + str(item.clockSpeed) + ",\n")
        file_microcontroller.write("\t\t\"userCreation\" : " + str(item.userCreation_id) + ",\n")
        file_microcontroller.write("\t\t\"userAmendment\" : " + str(item.userAmendment_id) + ",\n")
        file_microcontroller.write("\t\t\"dateTimeCreation\" : \"" + str(item.dateTimeCreation) + "\",\n")
        file_microcontroller.write("\t\t\"dateTimeChange\" : \"" + str(item.dateTimeChange) + "\"\n")
        file_microcontroller.write("\t}\n")
        if qt > 1:
            file_microcontroller.write("},\n")
        else:
            file_microcontroller.write("}\n")
        qt -= 1    
    file_microcontroller.write("]\n")    
    file_microcontroller.close()
    
    
    microComputer = Microcomputer.objects.filter()
    
    file_microComputer = open("iot/fixtures/microComputer.json", "w")
    file_microComputer.write("[\n")
    qt = len(microComputer)
    for item in microComputer:
        file_microComputer.write("\t{\n")
        file_microComputer.write("\t\t\"model\": \"iot.Microcomputer\",\n")
        file_microComputer.write("\t\t\"pk\": \"" + str(item.id) + "\",\n")
        file_microComputer.write("\t\t\"fields\": {\n")
        file_microComputer.write("\t\t\"name\" : \"" + (item.name).encode("utf-8\n") + "\",\n")
        file_microComputer.write("\t\t\"model\" : \"" + (item.model).encode("utf-8\n") + "\",\n")
        if item.processor_id==None:
            file_microComputer.write("\t\t\"processor\" : null,\n")
        else:
            file_microComputer.write("\t\t\"processor\" : " + str(item.processor_id) + ",\n")
        if item.microcontroller_id==None:
            file_microComputer.write("\t\t\"microcontroller\" : null,\n")
        else:
            file_microComputer.write("\t\t\"microcontroller\" : " + str(item.microcontroller_id) + ",\n")
        if item.GPU_id==None:
            file_microComputer.write("\t\t\"GPU\" : null,\n")
        else:
            file_microComputer.write("\t\t\"GPU\" : " + str(item.GPU_id) + ",\n")
        if item.operatingSystems_id==None:   
            file_microComputer.write("\t\t\"operatingSystems\" : null,\n") 
        else:
            file_microComputer.write("\t\t\"operatingSystems\" : " + str(item.operatingSystems_id) + ",\n")
        file_microComputer.write("\t\t\"dateManufacture\" : \"" + str(item.dateManufacture) + "\",\n")
        file_microComputer.write("\t\t\"userCreation\" : " + str(item.userCreation_id) + ",\n")
        file_microComputer.write("\t\t\"userAmendment\" : " + str(item.userAmendment_id) + ",\n")
        file_microComputer.write("\t\t\"dateTimeCreation\" : \"" + str(item.dateTimeCreation) + "\",\n")
        file_microComputer.write("\t\t\"dateTimeChange\" : \"" + str(item.dateTimeChange) + "\"\n")
        file_microComputer.write("\t}\n")
        if qt > 1:
            file_microComputer.write("},\n")
        else:
            file_microComputer.write("}\n")
        qt -= 1    
    file_microComputer.write("]\n")    
    file_microComputer.close()
    
    
    caracteristica = PhysicalCharacteristic.objects.filter()
    
    file_caracteristica = open("iot/fixtures/physicalCharacteristic.json", "w")
    file_caracteristica.write("[\n")
    qt = len(caracteristica)

    for item in caracteristica:
        file_caracteristica.write("\t{\n")
        file_caracteristica.write("\t\t\"model\": \"iot.PhysicalCharacteristic\",\n")
        file_caracteristica.write("\t\t\"pk\": " + str(item.id) + ",\n")
        file_caracteristica.write("\t\t\"fields\": {\n")
        file_caracteristica.write("\t\t\"microComputer\" : " + str(item.microComputer_id) + ",\n")
        file_caracteristica.write("\t\t\"length\" : " + str(item.length) + ",\n")
        file_caracteristica.write("\t\t\"width\" : " + str(item.width) + ",\n")
        file_caracteristica.write("\t\t\"weight\" : " + str(item.weight) + "\n")
        file_caracteristica.write("\t}\n")
        if qt > 1:
            file_caracteristica.write("},\n")
        else:
            file_caracteristica.write("}\n")
        qt -= 1    
    file_caracteristica.write("]\n")    
    file_caracteristica.close()
    
    
    gpu = GPU.objects.filter()
    
    file_gpu = open("iot/fixtures/gpu.json", "w")
    file_gpu.write("[\n")
    qt = len(gpu)
    for item in gpu:
        file_gpu.write("\t{\n")
        file_gpu.write("\t\t\"model\": \"iot.GPU\",\n")
        file_gpu.write("\t\t\"pk\": " + str(item.id) + ",\n")
        file_gpu.write("\t\t\"fields\": {\n")
        file_gpu.write("\t\t\"type\" : \"" + (item.type).encode("utf-8\n") + "\",\n")
        file_gpu.write("\t\t\"clockSpeed\" : " + str(item.clockSpeed) + ",\n")
        file_gpu.write("\t\t\"userCreation\" : " + str(item.userCreation_id) + ",\n")
        file_gpu.write("\t\t\"userAmendment\" : " + str(item.userAmendment_id) + ",\n")
        file_gpu.write("\t\t\"dateTimeCreation\" : \"" + str(item.dateTimeCreation) + "\",\n")
        file_gpu.write("\t\t\"dateTimeChange\" : \"" + str(item.dateTimeChange) + "\"\n")
        file_gpu.write("\t}\n")
        if qt > 1:
            file_gpu.write("},\n")
        else:
            file_gpu.write("}\n")
        qt -= 1    
    file_gpu.write("]\n")    
    file_gpu.close()
    
    
    memory = Memory.objects.filter()
    
    file_memory = open("iot/fixtures/memory.json", "w")
    file_memory.write("[\n")
    qt = len(memory)

    for item in memory:
        file_memory.write("\t{\n")
        file_memory.write("\t\t\"model\": \"iot.Memory\",\n")
        file_memory.write("\t\t\"pk\": " + str(item.id) + ",\n")
        file_memory.write("\t\t\"fields\": {\n")
        file_memory.write("\t\t\"microComputer\" : " + str(item.microComputer_id) + ",\n")
        file_memory.write("\t\t\"RAM\" : \"" + str(item.RAM) + "\",\n")
        file_memory.write("\t\t\"SRAM\" : \"" + str(item.SRAM) + "\",\n")
        file_memory.write("\t\t\"EEPROM\" : \"" + str(item.EEPROM) + "\",\n")
        file_memory.write("\t\t\"flashMemory\" : \"" + str(item.flashMemory) + "\"\n")
        file_memory.write("\t}\n")
        if qt > 1:
            print " > 1", qt
            file_memory.write("},\n")
        else:
            print " == 1", qt
            file_memory.write("}\n")
        qt -= 1    
    file_memory.write("]\n")    
    file_memory.close()
    
    
    voltage = Voltage.objects.filter()
    
    file_voltage = open("iot/fixtures/voltage.json", "w")
    file_voltage.write("[\n")
    qt = len(voltage)

    for item in voltage:
        file_voltage.write("\t{\n")
        file_voltage.write("\t\t\"model\": \"iot.Voltage\",\n")
        file_voltage.write("\t\t\"pk\": " + str(item.id) + ",\n")
        file_voltage.write("\t\t\"fields\": {\n")
        file_voltage.write("\t\t\"microComputer\" : " + str(item.microComputer_id) + ",\n")
        file_voltage.write("\t\t\"operatingVoltage\" : " + str(item.operatingVoltage) + ",\n")
        file_voltage.write("\t\t\"inputVoltageRecommended\" : \"" + str(item.inputVoltageRecommended) + "\",\n")
        file_voltage.write("\t\t\"IOCurrentMax\" : \"" + str(item.IOCurrentMax) + "\",\n")
        file_voltage.write("\t\t\"DCCurrentfor3_3VPin\" : \"" + str(item.DCCurrentfor3_3VPin) + "\",\n")
        file_voltage.write("\t\t\"powerRatings\" : \"" + str(item.powerRatings) + "\",\n")
        file_voltage.write("\t\t\"powerSource\" : \"" + str(item.powerSource) + "\"\n")
        file_voltage.write("\t}\n")
        if qt > 1:
            print " > 1", qt
            file_voltage.write("},\n")
        else:
            print " == 1", qt
            file_voltage.write("}\n")
        qt -= 1    
    file_voltage.write("]\n")    
    file_voltage.close()


    
    interface = Interface.objects.filter()
    
    file_interface = open("iot/fixtures/interface.json", "w")
    file_interface.write("[\n")
    qt = len(interface)
    for item in interface:
        file_interface.write("\t{\n")
        file_interface.write("\t\t\"model\": \"iot.Interface\",\n")
        file_interface.write("\t\t\"pk\": \"" + str(item.id) + "\",\n")
        file_interface.write("\t\t\"fields\": {\n")
        file_interface.write("\t\t\"microComputer\" : " + str(item.microComputer_id) + ",\n")
        file_interface.write("\t\t\"hdmi\" : \"" + (item.hdmi).encode("utf-8\n") + "\",\n")
        file_interface.write("\t\t\"videoInput\" : \"" + (item.videoInput).encode("utf-8\n") + "\",\n")
        file_interface.write("\t\t\"videoOutputs\" : \"" + (item.videoOutputs).encode("utf-8\n") + "\",\n")
        file_interface.write("\t\t\"audioInputs\" : \"" + (item.audioInputs).encode("utf-8\n") + "\",\n")
        file_interface.write("\t\t\"audioOutputs\" : \"" + (item.audioOutputs).encode("utf-8\n") + "\",\n")
        file_interface.write("\t\t\"storage\" : \"" + (item.storage).encode("utf-8\n") + "\",\n")
        file_interface.write("\t\t\"network\" : \"" + (item.network).encode("utf-8\n") + "\",\n")
        file_interface.write("\t\t\"wifi\" : \"" + (item.wifi).encode("utf-8\n") + "\",\n")
        file_interface.write("\t\t\"jack\" : \"" + (item.jack).encode("utf-8\n") + "\",\n")
        file_interface.write("\t\t\"GPIO\" : \"" + (item.GPIO).encode("utf-8\n") + "\",\n")
        file_interface.write("\t\t\"digitalIOPins\" : " + str(item.digitalIOPins) + ",\n")
        file_interface.write("\t\t\"analogInputPins\" : " + str(item.analogInputPins) + "\n")
        file_interface.write("\t}\n")
        if qt > 1:
            file_interface.write("},\n")
        else:
            file_interface.write("}\n")
        qt -= 1    
    file_interface.write("]\n")    
    file_interface.close()
    
    
    processor = Processor.objects.filter()
    
    file_processor = open("iot/fixtures/processor.json", "w")
    file_processor.write("[\n")
    qt = len(processor)
    for item in processor:
        file_processor.write("\t{\n")
        file_processor.write("\t\t\"model\": \"iot.Processor\",\n")
        file_processor.write("\t\t\"pk\": " + str(item.id) + ",\n")
        file_processor.write("\t\t\"fields\": {\n")
        file_processor.write("\t\t\"type\" : \"" + (item.type).encode("utf-8\n") + "\",\n")
        file_processor.write("\t\t\"clockSpeed\" : " + str(item.clockSpeed) + ",\n")
        file_processor.write("\t\t\"userCreation\" : " + str(item.userCreation_id) + ",\n")
        file_processor.write("\t\t\"userAmendment\" : " + str(item.userAmendment_id) + ",\n")
        file_processor.write("\t\t\"dateTimeCreation\" : \"" + str(item.dateTimeCreation) + "\",\n")
        file_processor.write("\t\t\"dateTimeChange\" : \"" + str(item.dateTimeChange) + "\"\n")
        file_processor.write("\t}\n")
        if qt > 1:
            file_processor.write("},\n")
        else:
            file_processor.write("}\n")
        qt -= 1    
    file_processor.write("]\n")    
    file_processor.close()
    
    
    sensor = Sensor.objects.filter()
    
    file_sensor = open("iot/fixtures/sensor.json", "w")
    file_sensor.write("[\n")
    qt = len(sensor)
    for item in sensor:
        file_sensor.write("\t{\n")
        file_sensor.write("\t\t\"model\": \"iot.Sensor\",\n")
        file_sensor.write("\t\t\"pk\": " + str(item.id) + ",\n")
        file_sensor.write("\t\t\"fields\": {\n")
        file_sensor.write("\t\t\"name\" : \"" + (item.name).encode("utf-8\n") + "\",\n")
        file_sensor.write("\t\t\"serialNumber\" : \"" + (item.serialNumber).encode("utf-8\n") + "\",\n")
        file_sensor.write("\t\t\"model\" : \"" + (item.model).encode("utf-8\n") + "\",\n")
        file_sensor.write("\t\t\"function\" : \"" + (item.function).encode("utf-8\n") + "\"\n")
        file_sensor.write("\t}\n")
        if qt > 1:
            file_sensor.write("},\n")
        else:
            file_sensor.write("}\n")
        qt -= 1    
    file_sensor.write("]\n")    
    file_sensor.close()
    
    template = Template.objects.filter()
    
    file_template = open("iot/fixtures/template.json", "w")
    file_template.write("[\n")
    qt = len(template)
    for item in template:
        file_template.write("\t{\n")
        file_template.write("\t\t\"model\": \"iot.Template\",\n")
        file_template.write("\t\t\"pk\": " + str(item.id) + ",\n")
        file_template.write("\t\t\"fields\": {\n")
        file_template.write("\t\t\"name\" : \"" + (item.name).encode("utf-8\n") + "\",\n")
        file_template.write("\t\t\"imagePath\" : \"" + (item.imagePath).encode("utf-8\n") + "\"\n")
        #---------------------------------------------------- for i in template:
            #--------------------------------------- for j in i.equipment.all():
                # file_template.write("\t\t\"equipment\" : " + str(j.id) + ",\n")
            
        file_template.write("\t}\n")
        if qt > 1:
            file_template.write("},\n")
        else:
            file_template.write("}\n")
        qt -= 1    
    file_template.write("]\n")    
    file_template.close()
    
        
    return HttpResponse("Ficheiros gerados com sucesso!\n")

