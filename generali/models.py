from statistics import mode
from django.db import models


class Formulario(models.Model):
    client_choices = (
        ('N','Nuevo'),
        ('R','Renovacion'),
    )
    ramo_choices = (
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
    typeid_choices = (
        ('Cedula','Cedula'),
        ('Pasaporte','Pasaporte'),
        ('RUC','RUC'),
    )
    sex_choices = (
        ('M','M'),
        ('F','F'),
    )
    civilstat_choices = (
        ('Soltero','Soltero'),
        ('Casado','Casado'),
        ('Divorciado','Divorciado'),
        ('U/Libre','U/Libre'),
        ('Viudo','Viudo'),
        ('Separado','Separado'),
    )
    city_choices = (
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
    )
    prov_choices = (
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
    )
    bond_choices = (
        ('Familiar','Familiar'),
        ('Comercial','Comercial'),
        ('Laboral','Laboral'),
        ('Ninguna','Ninguna'),
        ('Otros','Otros')
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
    state_solicit = models.CharField(max_length = 200, choices = stateciv_choices)
    nacim_solicit = mdoels.CharField(max_length = 200)
    datenacim_solict = models.CharField(max_length = 200)
    nacio_solicit = models.CharField(max_length = 200)
    domic_solicit = models.CharField(max_length = 200)
    ciud_solicit = models.CharField(max_length = 200)
    pais_solicit
    prov_solicit
    tel_solicit
    email_solicit
    mail_fact_solicit
    mail_form_solicit
    contac_solicit
    con_doc_solicit
    
