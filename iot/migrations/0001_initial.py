# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import audit_log.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('type', models.CharField(max_length=100, verbose_name=b'Tipo', blank=True)),
                ('dateTimeCreation', models.DateTimeField(auto_now_add=True)),
                ('dateTimeChange', models.DateTimeField(auto_now=True)),
                ('userAmendment', audit_log.models.fields.LastUserField(editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('userCreation', audit_log.models.fields.CreatingUserField(related_name='created_accessory', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Acess\xf3rio',
                'verbose_name_plural': 'Acess\xf3rios',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('model', models.CharField(max_length=100, verbose_name=b'Modelo', blank=True)),
                ('serialNumber', models.CharField(max_length=100, verbose_name=b'N\xc3\xbamero de S\xc3\xa9rie')),
                ('dateTimeCreation', models.DateTimeField(auto_now_add=True)),
                ('dateTimeChange', models.DateTimeField(auto_now=True)),
                ('accessory', models.ManyToManyField(to='iot.Accessory', verbose_name=b'Acess\xc3\xb3rio', blank=True)),
            ],
            options={
                'verbose_name': 'Equipamento',
                'verbose_name_plural': 'Equipamentos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Expansion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100, verbose_name=b'Tipo')),
                ('peripherals', models.CharField(max_length=100, verbose_name=b'Perif\xc3\xa9ricos', blank=True)),
                ('dateTimeCreation', models.DateTimeField(auto_now_add=True)),
                ('dateTimeChange', models.DateTimeField(auto_now=True)),
                ('userAmendment', audit_log.models.fields.LastUserField(editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('userCreation', audit_log.models.fields.CreatingUserField(related_name='created_expansions', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Expans\xe3o',
                'verbose_name_plural': 'Expans\xf5es',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100, verbose_name=b'Tipo')),
                ('clockSpeed', models.IntegerField(verbose_name=b'Clock Speed MHz')),
                ('dateTimeCreation', models.DateTimeField(auto_now_add=True)),
                ('dateTimeChange', models.DateTimeField(auto_now=True)),
                ('userAmendment', audit_log.models.fields.LastUserField(editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('userCreation', audit_log.models.fields.CreatingUserField(related_name='created_gpus', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'GPU',
                'verbose_name_plural': 'GPUs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hdmi', models.CharField(max_length=100, blank=True)),
                ('USBPorts', models.CharField(max_length=100, verbose_name=b'Porta USB', blank=True)),
                ('videoInput', models.CharField(max_length=100, verbose_name=b'Entrada de v\xc3\xaddeo', blank=True)),
                ('videoOutputs', models.CharField(max_length=100, verbose_name=b'Saida de v\xc3\xaddeo', blank=True)),
                ('audioInputs', models.CharField(max_length=100, verbose_name=b'Entrada de audio', blank=True)),
                ('audioOutputs', models.CharField(max_length=100, verbose_name=b'Saida de audio', blank=True)),
                ('storage', models.CharField(max_length=100, verbose_name=b'Armazenamento', blank=True)),
                ('network', models.CharField(max_length=100, verbose_name=b'Rede', blank=True)),
                ('wifi', models.CharField(max_length=100, verbose_name=b'WiFi', blank=True)),
                ('jack', models.CharField(max_length=100, blank=True)),
                ('GPIO', models.CharField(max_length=100, blank=True)),
                ('digitalIOPins', models.IntegerField(default=0, verbose_name=b'Pinos I/O digital')),
                ('analogInputPins', models.IntegerField(default=0, verbose_name=b'Pinos de entrada anal\xc3\xb3gica')),
            ],
            options={
                'verbose_name': 'Interface',
                'verbose_name_plural': 'Interfaces',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('RAM', models.FloatField(default=0, verbose_name=b'RAM')),
                ('quantidadeRAM', models.CharField(default=b'KB', max_length=2, verbose_name=b'Quantidade em', choices=[(b'KB', b'KB'), (b'MB', b'MB'), (b'GB', b'GB')])),
                ('SRAM', models.FloatField(default=0, verbose_name=b'SRAM KB')),
                ('EEPROM', models.FloatField(default=0, verbose_name=b'EEPROM KB')),
                ('flashMemory', models.FloatField(default=0, verbose_name=b'Mem\xc3\xb3ria Flash')),
                ('quantidadeFlashMemory', models.CharField(default=b'KB', max_length=2, verbose_name=b'Quantidade em', choices=[(b'KB', b'KB'), (b'MB', b'MB'), (b'GB', b'GB')])),
            ],
            options={
                'verbose_name': 'Mem\xf3ria',
                'verbose_name_plural': 'Mem\xf3rias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Microcomputer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('model', models.CharField(max_length=100, verbose_name=b'Modelo')),
                ('dateManufacture', models.DateField(verbose_name=b'Data de Fabrico')),
                ('dateTimeCreation', models.DateTimeField(auto_now_add=True)),
                ('dateTimeChange', models.DateTimeField(auto_now=True)),
                ('GPU', models.ForeignKey(blank=True, to='iot.GPU', null=True)),
            ],
            options={
                'verbose_name': 'Microcomputador',
                'verbose_name_plural': 'Microcomputadores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Microcontroller',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100, verbose_name=b'Microcontrolador')),
                ('clockSpeed', models.IntegerField(verbose_name=b'Clock Speed MHz')),
                ('dateTimeCreation', models.DateTimeField(auto_now_add=True)),
                ('dateTimeChange', models.DateTimeField(auto_now=True)),
                ('userAmendment', audit_log.models.fields.LastUserField(editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('userCreation', audit_log.models.fields.CreatingUserField(related_name='created_microcontroller', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Microcontrolador',
                'verbose_name_plural': 'Microcontroladores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('version', models.CharField(max_length=100, verbose_name=b'Vers\xc3\xa3o', blank=True)),
                ('dateTimeCreation', models.DateTimeField(auto_now_add=True)),
                ('dateTimeChange', models.DateTimeField(auto_now=True)),
                ('userAmendment', audit_log.models.fields.LastUserField(editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('userCreation', audit_log.models.fields.CreatingUserField(related_name='created_operationsystems', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Sistema Operativo',
                'verbose_name_plural': 'Sistemas Operativos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhysicalCharacteristic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('length', models.FloatField(default=0, verbose_name=b'Comprimento (mm)')),
                ('width', models.FloatField(default=0, verbose_name=b'Largura (mm)')),
                ('weight', models.FloatField(default=0, verbose_name=b'Peso (g)')),
                ('microComputer', models.ForeignKey(verbose_name=b'Microcomputador', to='iot.Microcomputer')),
            ],
            options={
                'verbose_name': 'Caracter\xedstica F\xedsica',
                'verbose_name_plural': 'Caracter\xedsticas F\xedsicas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100, verbose_name=b'Processador')),
                ('clockSpeed', models.IntegerField(verbose_name=b'Clock Speed MHz')),
                ('dateTimeCreation', models.DateTimeField(auto_now_add=True)),
                ('dateTimeChange', models.DateTimeField(auto_now=True)),
                ('userAmendment', audit_log.models.fields.LastUserField(editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('userCreation', audit_log.models.fields.CreatingUserField(related_name='created_processor', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Processador',
                'verbose_name_plural': 'Processadores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReadData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField(verbose_name=b'Temperatura')),
                ('humidity', models.FloatField(verbose_name=b'Humidade')),
                ('dateTimeCreation', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelativePosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nameElement', models.CharField(max_length=100)),
                ('leftX', models.FloatField(default=0.0)),
                ('topY', models.FloatField(default=0.0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('serialNumber', models.CharField(max_length=100, verbose_name=b'N\xc3\xbamero de S\xc3\xa9rie')),
                ('model', models.CharField(max_length=100, null=True, verbose_name=b'Modelo')),
                ('function', models.CharField(max_length=100, null=True, verbose_name=b'Fun\xc3\xa7\xc3\xa3o')),
            ],
            options={
                'verbose_name': 'Sensor',
                'verbose_name_plural': 'Sensores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome do Template')),
                ('imagePath', models.FileField(upload_to=b'static', blank=True)),
                ('equipment', models.ManyToManyField(to='iot.Equipment', verbose_name=b'Equipamentos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Voltage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operatingVoltage', models.FloatField(default=0, verbose_name=b'Voltagem Operacional (V)')),
                ('inputVoltageRecommended', models.CharField(default=0, max_length=10, verbose_name=b'Voltagem recomendada (V)')),
                ('IOCurrentMax', models.CharField(default=0, max_length=10, verbose_name=b'I/O Corrente limites (V)')),
                ('DCCurrentperIOPin', models.IntegerField(default=0, verbose_name=b'DC Corrente por pino (mA)')),
                ('DCCurrentfor3_3VPin', models.IntegerField(default=0, verbose_name=b'DC Corrente por 3.3 pino (mA)')),
                ('powerRatings', models.CharField(max_length=100, verbose_name=b'Classifica\xc3\xa7\xc3\xb5es de energia', blank=True)),
                ('powerSource', models.CharField(max_length=100, verbose_name=b'Fonte de energia', blank=True)),
                ('microComputer', models.ForeignKey(verbose_name=b'Microcomputador', to='iot.Microcomputer')),
            ],
            options={
                'verbose_name': 'Voltagem',
                'verbose_name_plural': 'Voltagens',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='microcomputer',
            name='microcontroller',
            field=models.ForeignKey(verbose_name=b'Microcontrolador', blank=True, to='iot.Microcontroller', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='microcomputer',
            name='operatingSystems',
            field=models.ForeignKey(verbose_name=b'Sistema Operativo', blank=True, to='iot.OperatingSystem', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='microcomputer',
            name='processor',
            field=models.ForeignKey(verbose_name=b'Processador', blank=True, to='iot.Processor', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='microcomputer',
            name='userAmendment',
            field=audit_log.models.fields.LastUserField(editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='microcomputer',
            name='userCreation',
            field=audit_log.models.fields.CreatingUserField(related_name='created_microcomputer', editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='memory',
            name='microComputer',
            field=models.ForeignKey(verbose_name=b'Microcomputador', to='iot.Microcomputer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='interface',
            name='microComputer',
            field=models.ForeignKey(verbose_name=b'Microcomputador', to='iot.Microcomputer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipment',
            name='expansion',
            field=models.ManyToManyField(to='iot.Expansion', verbose_name=b'Expans\xc3\xa3o', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipment',
            name='microComputer',
            field=models.ForeignKey(verbose_name=b'Microcomputador', to='iot.Microcomputer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipment',
            name='sensor',
            field=models.ManyToManyField(to='iot.Sensor', verbose_name=b'Sensor', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipment',
            name='userAmendment',
            field=audit_log.models.fields.LastUserField(editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipment',
            name='userCreation',
            field=audit_log.models.fields.CreatingUserField(related_name='created_equipments', editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
