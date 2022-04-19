from statistics import mode
from django.db import models


class Formulario(models.Model):
    cliente_choices = (
        ('N','Nuevo'),
        ('R','Renovacion'),
    )
    tiposeguro_choices = (
        ('vehiculo','VEHICULOS'),
        ('vidagrupal','VIDA EN GRUPO'),
        ('vidaindividuak','VIDA INDIVIDUAL'),
        ('incendio','INCENDIO'),
        ('transporte','TRANSPORTE'),
        ('contratistas','CONTRATISTAS'),
        ('casoaviones','CASCO DE AVIONES'),
        ('accidentepersonal','ACCIDENTES PERSONALES'),
        ('asistenciamedica','ASISTENCIA MEDICA'),
        ('equipoelectronico','EQUIPO ELECTRONICO'),
        ('robo','ROBO'),
        ('responsabilidadcivil','RESPONSABILIDAD CIVIL'),
        ('roturamaquinaria','ROTURA DE MAQUINARIA'),
        ('cascobuque','CASCO DE BUQUE'),
        ('cumplimientocontrato','CUMPLIMIENTO DE CONTRATO'),
        ('fidelidad','FIDELIDAD'),
        ('montajeriesgo','MONTAJE TODO RIESGO'),
        ('salud','SALUD'),
    )
    tipoid_choices = (
        ('Cedula','Cedula'),
        ('Pasaporte','Pasaporte'),
        ('RUC','RUC'),
    )
    sexo_choices = (
        ('M','M'),
        ('F','F'),
        )
    
    cliente = models.TextChoices(
        max_length = 200,
        choices = cliente_choices.choices,
        verbose_name = "cliente")
    tiposeguro = models.CharField(
        max_length = 200,
        choices = tiposeguro_choices)
    sumasegurada = models.IntegerField()

    doc_solicit = models.CharField(max_length = 200, choices = tipoid_choices)
    num_solicit = models.IntegerField()
    apell_solicit = models.CharField(max_length = 200)
    name_solicit = models.CharField(max_length = 200)

    sex_solicit = models.CharField(max_length = 200, choices = sexo_choices)
    

    
