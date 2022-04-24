from statistics import mode
from django.db import models


class Formulario(models.Model):
    cliente = models.CharField(max_length = 200)
    tiposeguro = models.CharField(max_length = 200)
    sumasegurada = models.IntegerField()
    
    doc_solicit = models.CharField(max_length = 200)
    num_solicit = models.IntegerField()
    apell_solicit = models.CharField(max_length = 200)
    name_solicit = models.CharField(max_length = 200)
    sex_solicit = models.CharField(max_length = 200)
    state_solicit = models.CharField(max_length = 200)
    nacim_solicit = models.CharField(max_length = 200)
    datenacim_solict = models.DateField(blank = True, null = True)
    nacion_solicit = models.CharField(max_length = 200)
    domic_solicit = models.CharField(max_length = 200)
    ciud_solicit = models.CharField(max_length = 200)
    pais_solicit = models.CharField(max_length = 200)
    prov_solicit = models.CharField(max_length = 200)
    tel_solicit = models.IntegerField()
    mail_solicit = models.EmailField(max_length = 200)
    mail_fact_solicit = models.EmailField(max_length = 200)
    mail_form_solicit = models.EmailField(max_length = 200)
    contac_solicit = models.CharField(max_length = 200)
    
    doc_conv = models.CharField(max_length = 200)
    num_conv = models.IntegerField()
    apell_conv = models.CharField(max_length = 200)
    name_conv = models.CharField(max_length = 200)

    vinc_asegur = models.CharField(max_length = 200)
    specif_asegur = models.CharField(max_length = 200)
    doc_asegur = models.CharField(max_length = 200)
    num_asegur = models.IntegerField()
    apell_asegur = models.CharField(max_length = 200)
    name_asegur = models.CharField(max_length = 200)
    sex_asegur = models.CharField(max_length = 200)
    state_asegur = models.CharField(max_length = 200)
    nacim_asegur = models.CharField(max_length = 200)
    datenacim_asegur = models.DateField(blank=True, null=True)
    nacion_asegur = models.CharField(max_length = 200)
    domic_asegur = models.CharField(max_length = 200)
    tel_asegur = models.IntegerField()
    mail_asegur = models.EmailField(max_length = 200)

    vinc_benefic = models.CharField(max_length = 200)
    specif_benefic = models.CharField(max_length = 200)
    doc_benefic = models.CharField(max_length = 200)
    num_benefic = models.IntegerField()
    apell_benefic = models.CharField(max_length = 200)
    name_benefic = models.CharField(max_length = 200)
    sex_benefic = models.CharField(max_length = 200)
    state_benefic = models.CharField(max_length = 200)
    nacim_benefic = models.CharField(max_length = 200)
    datenacim_benefic = models.DateField(blank = True, null = True)
    nacion_benefic = models.CharField(max_length = 200)
    domic_benefic = models.CharField(max_length = 200)
    tel_benefic = models.IntegerField()
    mail_benefic = models.EmailField(max_length = 200)

    type_work = models.CharField(max_length = 200)
    especify_work = models.CharField(max_length = 200)
    razon_work = models.CharField(max_length = 200)
    sector_work = models.CharField(max_length = 200)
    activity_work = models.CharField(max_length = 200)
    cargo_work = models.CharField(max_length = 200)
    domic_work = models.CharField(max_length = 200)
    city_work = models.CharField(max_length = 200)
    ciud_work = models.CharField(max_length = 200)
    mail_work = models.EmailField(max_length = 200)
    tel_work = models.IntegerField()

    ingress_info = models.IntegerField()
    mesuality_info = models.IntegerField()
    other_info = models.IntegerField()
    activos_info = models.IntegerField()
    pasivos_info = models.IntegerField()
    patrim_info = models.IntegerField()

    name_reference = models.CharField(max_length = 200)
    parentesc_reference = models.CharField(max_length = 200)
    tel_reference = models.IntegerField()
    target_reference = models.CharField(max_length = 200)
    instfin_reference = models.CharField(max_length = 200)
    ctatype_reference = models.CharField(max_length = 200)
    instbanc_reference = models.CharField(max_length = 200)
    nameoth_reference = models.CharField(max_length = 200)
    parentescoth_reference = models.CharField(max_length = 200)
    teloth_reference = models.CharField(max_length = 200)
    targetoth_reference = models.CharField(max_length = 200)
    instfinoth_reference = models.CharField(max_length = 200)
    ctatypeoth_reference = models.CharField(max_length = 200)
    instbancoth_reference = models.CharField(max_length = 200)

    emision_factur = models.CharField(max_length = 200)
    social_factur = models.CharField(max_length = 200)
    rucci_factur = models.IntegerField()
    tel_factur = models.IntegerField()
    domic_factur = models.CharField(max_length = 200)
    relacion_factur = models.CharField(max_length = 200)

    names_extra = models.CharField(max_length = 200)
    adicionch_extra = models.CharField(max_length = 200)
    specific_extra = models.CharField(max_length = 200)
    func_extra = models.CharField(max_length = 200)
    
    cargo_extra_decl = models.CharField(max_length = 200)
    datenacim_decl = models.DateField(blank = True, null = True)
    datenacim_extra_decl = models.DateField(blank = True, null = True)
    politic_decl = models.CharField(max_length = 200)
    specif_decl = models.CharField(max_length = 200)
    con_decl = models.CharField(max_length = 200)


    canal_extra = models.CharField(max_length = 200)

    ced_file = models.FileField(blank = True, null = True,
        upload_to ='chapters/%Y/%m/%D/')
    serbas_file = models.FileField(blank = True, null = True,
        upload_to ='chapters/%Y/%m/%D/')
    conv_file = models.FileField(blank = True, null = True,
        upload_to ='chapters/%Y/%m/%D/')
    cert_file = models.FileField(blank = True, null = True,
        upload_to ='chapters/%Y/%m/%D/')
    cargo_file = models.FileField(blank = True, null = True,
        upload_to ='chapters/%Y/%m/%D/')
    renta_file = models.FileField(blank = True, null = True,
        upload_to ='chapters/%Y/%m/%D/')

    lugar_declaration = models.CharField(max_length = 200)
    condic_declaration = models.CharField(max_length = 200)