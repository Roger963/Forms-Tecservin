from cProfile import label
from django.forms import ModelForm
from django import forms
from .models import Formulario

class FormularioForm(ModelForm):
  
    class Meta:
        client_choices = [('N','Nuevo'),('R','Renovacion'),]
        ramo_choices = (('vehiculo','VEHICULOS'),('vidagrupal','VIDA EN GRUPO'),('vidaindividuak','VIDA INDIVIDUAL'),('incendio','INCENDIO'),('transporte','TRANSPORTE'),('contratistas','CONTRATISTAS'),('casoaviones','CASCO DE AVIONES'),('accidentepersonal','ACCIDENTES PERSONALES'),('asistenciamedica','ASISTENCIA MEDICA'),('equipoelectronico','EQUIPO ELECTRONICO'),('robo','ROBO'),('responsabilidadcivil','RESPONSABILIDAD CIVIL'),('roturamaquinaria','ROTURA DE MAQUINARIA'),('cascobuque','CASCO DE BUQUE'),('cumplimientocontrato','CUMPLIMIENTO DE CONTRATO'),('fidelidad','FIDELIDAD'),('montajeriesgo','MONTAJE TODO RIESGO'),('salud','SALUD'),)
        sex_choices = (('M','M'),('F','F'),)
        civilstat_choices = (('Soltero','Soltero'),('Casado','Casado'),('Divorciado','Divorciado'),('U/Libre','U/Libre'),('Viudo','Viudo'),('Separado','Separado'),)
        typeid_choices = (('Cedula','Cedula'),('Pasaporte','Pasaporte'),('RUC','RUC'),)
        bond_choices = (('Familiar','Familiar'),('Comercial','Comercial'),('Laboral','Laboral'),('Ninguna','Ninguna'),('Otros','Otros'))
        vinculo_choices = (('Familiar','Familiar'),('Comercial','Comercial'),('Laboral','Laboral '),('Ninguna','Ninguna'), ('Otros', 'Otros'))

        prov_choices = (('AZUAY','AZUAY'),('BOLIVAR','BOLIVAR'),('CAÑAR','CAÑAR'),('CARCHI','CARCHI'),('CHIMBORAZO','CHIMBORAZO'),('COTOPAXI','COTOPAXI'),
        ('EL ORO','EL ORO'),('ESMERALDAS','ESMERALDAS'),('GALAPAGOS','GALAPAGOS'),('GUAYAS','GUAYAS'),('IMBABURA','IMBABURA'),('LOJA','LOJA'),('LOS RIOS','LOS RIOS'),
        ('MANABI','MANABI'),('MORRONA SANTIAGO','MORRONA SANTIAGO'),('NAPO','NAPO'),('ORELLANA','ORELLANA'),('PASTAZA','PASTAZA'),('PICHINCHA','PICHINCHA'),
        ('SANTA ELENA','SANTA ELENA'),('SANTO DOMINGO DE LOS TSACHILAS','SANTO DOMINGO DE LOS TSACHILAS'),('SUCUMBIOS','SUCUMBIOS'),('TUNGURAHUA','TUNGURAHUA'),
        ('ZAMORA CHINCHIPE','ZAMORA CHINCHIPE'),)
        city_choices = (('AFG','AFGANISTAN'),('AX','ALAND'),('AL','ALBANIA'),('DEU','ALEMANIA'),('AD','ANDORRA'),('AO','ANGOLA'),('AI','ANGUILA'),('AQ','ANTARTIDA'),('AG','ANTIGUA Y BARBUDA'),('AN','ANTILLAS NEERLANDESAS'),('SA','ARABIA SAUDITA'),('DZ','ARGELIA'),('ARP','ARGENTINA'),('AM','ARMENIA'),('AW','ARUBA'),('AUD','AUSTRALIA'),('AT','AUSTRIA'),('AZ','AZERBAIYAN'),
            ('BS','BAHAMAS'),('BH','BAHREIN'),('BB','BARBADOS'),('BLR','BELARAUS'),('BE','BELGICA'),('BZ','BELICE'),('BJ','BENIN'),('BM','BERMUDAS'),('BY','BIELORRUSIA'),('MMR','BIRMANIA'),('BOL','BOLIVIA'),('BA','BOSNIA Y HERZEGOVINA'),('BW','BOTSUANA'),('BRC','BRASIL'),('BN','BRUNEI'),('BG','BULGARIA'),('BF','BURKINA FASO'),('BDI','BURUNDI'),('BT','BUTAN'),
            ('CV','CABO VERDE'),('KH','CAMBOYA'),('CM','CAMERUN'),('CAD','CANADA'),('TD','CHAD'),('CLP','CHILE'),('CHN','CHINA'),('CY','CHIPRE'),('VA','CIUDAD DEL VATICANO'),('COP','COLOMBIA'),('KM','COMORAS'),('PRK','COREA DEL NORTE'),('KR','COREA DEL SUR'),('CIV','COSTA DE MARFIL'),('CR','CRIMEA'),('HR','CROACIA'),('CUP','CUBA'),('DKK','DINAMARCA'),('DM','DOMINICA'),
            ('ECS','ECUADOR'),('EG','EGIPTO'),('SV','EL SALVADOR'),('AE','EMIRATOS ARABES UNIDOS'),('ERI','ERITREA'),('SK','ESLOVAQUIA'),('SI','ESLOVENIA'),('ESP','ESPA¥A'),('USA','ESTADOS UNIDOS'),('EE','ESTONIA'),('ET','ETIOPIA'),('PH','FILIPINAS'),('FI','FINLANDIA'),('FJ','FIYI'),('FRP','FRANCIA'),('GA','GABON'),('GM','GAMBIA'),('GE','GEORGIA'),('GH','GHANA'),('GD','GRANADA'),
            ('GR','GRECIA'),('GL','GROENLANDIA'),('GP','GUADALUPE'),('GU','GUAM'),('GTQ','GUATEMALA'),('GF','GUAYANA FRANCESA'),('GG','GUERNSEY'),('GIN','GUINE'),('GQ','GUINEA ECUATORIAL'),('GNB','GUINEA-BISSAU'),('GY','GUYANA'),('HTI','HAITI'),('NLG','HOLANDA'),('HN','HONDURAS'),('HK','HONG KONG'),('HU','HUNGRIA'),('IN','INDIA'),('ID','INDONESIA'),('ING','INGLATERRA'),
            ('IRR','IRAN'),('IRQ','IRAQ'),('IE','IRLANDA'),('BV','ISLA BOUVET'),('IM','ISLA DE MAN'),('CX','ISLA DE NAVIDAD'),('IS','ISLANDIA'),('KY','ISLAS CAIMáN'),('CC','ISLAS COCOS'),('CK','ISLAS COOK'),('FO','ISLAS FEROE'),('GS','ISLAS GEORGIAS DEL SUR Y SANDWICH DEL SUR'),('HM','ISLAS HEARD Y MCDONALD'),('FK','ISLAS MALVINAS'),('MP','ISLAS MARIANAS DEL NORTE'),
            ('MH','ISLAS MARSHALL'),('PN','ISLAS PITCAIRN'),('SB','ISLAS SALOMON'),('TC','ISLAS TURCAS Y CAICOS'),('UM','ISLAS ULTRAMARINAS DE ESTADOS UNIDOS'),('VG','ISLAS VIRGENES BRITANICAS'),('VI','ISLAS VIRGENES ESTADOUNIDENSES'),('IL','ISRAEL'),('ITA','ITALIA'),('JM','JAMAICA'),('JP','JAPON'),('JE','JERSEY'),('JO','JORDANIA'),('KZ','KAZAJISTAN'),('KE','KENIA'),
            ('KG','KIRGUISTAN'),('KI','KIRIBATI'),('KW','KUWAIT'),('LA','LAOS'),('LS','LESOTO'),('LV','LETONIA'),('LBN','LIBANO'),('LR','LIBERIA'),('LBY','LIBIA'),('LI','LIECHTENSTEIN'),('LT','LITUANIA'),('LU','LUXEMBURGO'),('MO','MACAO'),('MK','MACEDONIA'),('MG','MADAGASCAR'),('MY','MALASIA'),('MW','MALAUI'),('MV','MALDIVAS'),('MLI','MALI'),('MT','MALTA'),('MA','MARRUECOS'),
            ('MQ','MARTINICA'),('MU','MAURICIO'),('MR','MAURITANIA'),('YT','MAYOTTE'),('MXP','MEXICO'),('FM','MICRONESIA'),('MD','MOLDAVIA'),('MC','MONACO'),('MN','MONGOLIA'),('ME','MONTENEGRO'),('MS','MONTSERRAT'),('MZ','MOZAMBIQUE'),('MMR','MYANMAR'),('NA','NAMIBIA'),('NR','NAURU'),('NP','NEPAL'),('NIC','NICARAGUA'),('NE','NIGER'),('NG','NIGERIA'),('NU','NIUE'),('NF','NORFOLK'),
            ('NO','NORUEGA'),('NC','NUEVA CALEDONIA'),('NZ','NUEVA ZELANDA'),('OM','OMAN'),('NLD','PAISES BAJOS'),('PAK','PAKISTAN'),('PW','PALAOS'),('PAB','PANAMA'),('PG','PAPUA NUEVA GUINEA'),('PY','PARAGUAY'),('PES','PERU'),('PF','POLINESIA FRANCESA'),('PL','POLONIA'),('PT','PORTUGAL'),('QA','QATAR'),('GBR','REINO UNIDO'),('COD','REP.DEMOCRATICA DEL CONGLO'),
            ('CAF','REPUBLICA CENTROAFRICANA'),('CF','REPUBLICA CENTROAFRICANA'),('CZ','REPúBLICA CHECA'),('CG','REPUBLICA DEL CONGO'),('CD','REPUBLICA DEMOCRATICA'),('DO','REPUBLICA DOMINICANA'),('RE','REUNION'),('RW','RUANDA'),('ROS','RUMANIA'),('RUS','RUSIA'),('EH','SAHARA OCCIDENTAL'),('AS','SAMOA AMERICANA'),('BL','SAN BARTOLOMé'),('KN','SAN CRISTOBAL Y NIEVES'),('SM','SAN MARINO'),
            ('PM','SAN PEDRO Y MIQUELON'),('VC','SAN VICENTE Y LAS GRANADINAS'),('SH','SANTA HELENA'),('LC','SANTA LUCIA'),('ST','SANTO TOME Y PRINCIPE'),('SN','SENEGAL'),('RS','SERBIA'),('SC','SEYCHELLES'),('SL','SIERRA LEONA'),('SG','SINGAPUR'),('SYR','SIRIA'),('SOM','SOMALIA'),('SSD','SOUTH SUDAN'),('LK','SRI LANKA'),('SZ','SUAZILANDIA'),('ZA','SUDAFRICA'),
            ('SDN','SUDAN'),('SEK','SUECIA'),('CHF','SUIZA'),('SR','SURINAM'),('SJ','SVALBARD Y JAN MAYEN'),('TH','TAILANDIA'),('TW','TAIWAN'),('TZ','TANZANIA'),('TJ','TAYIKISTAN'),('IO','TERRITORIO BRITáNICO DEL OCéANO ÍNDICO'),('TF','TERRITORIOS AUSTRALES FRANCESES'),('PS','TERRITORIOS PALESTINOS'),('TL','TIMOR ORIENTAL'),('TG','TOGO'),('TK','TOKELAU'),('TO','TONGA'),
            ('TT','TRINIDAD Y TOBAGO'),('TN','TUNEZ'),('TM','TURKMENISTAN'),('TR','TURQUIA'),('TV','TUVALU'),('UKR','UCRANIA'),('UG','UGANDA'),('EU','UNION EUROPEA'),('SU','UNION SOVIETICA'),('UZ','URBEKISTAN'),('UYP','URUGUAY'),('VU','VANUATU'),('VEB','VENEZUELA'),('VN','VIETNAM'),('WF','WALLIS Y FUTUNA'),('YEM','YEMEN'),('DJ','YIBUTI'),('ZM','ZAMBIA'),('ZWE','ZIMBABUE'),)
        MEDIA_CHOICES = [
            ('Audio', (
                    ('vinyl', 'Vinyl'),('cd', 'CD'),)
            ),
            ('Video', (
                    ('vhs', 'VHS Tape'),('dvd', 'DVD'),) 
            ),
            ('unknown', 'Unknown'),
        ]
        
        model = Formulario
        fields = '__all__'
        labels = {
            'cliente':'CLIENTE',
            'tiposeguro' : 'Tipo de Seguro (Ramo)',
            'sumasegurada': 'Total Suma Asegurada USD',
            'doc_solicit': 'Tipo de ID',
            'num_solicit':'Número de ID',
            'apell_solicit':'Apellidos',
            'name_solicit':'Nombres',
            'sex_solicit':'Sexo',
            'state_solicit':'Estado Civil',
            'nacim_solicit':'Lugar de Nacimiento',
            'datenacim_solict':'Fecha de Nacimiento',
            'nacion_solicit':'Nacionalidad:',
            'domic_solict':'Domicilio',
            'ciud_solicit':'Ciudad',
            'pais_solicit':'País',
            'prov_solicit':'Provincia',
            'tel_solicit':'Telefonos',
            'mail_solicit':'E-mail',
            'mail_fact_solicit':'Mail para  recibir Factura Electrónica',
            'mail_form_solicit':'Mail  para recibir el Formulario de Retención',
            'contac_solicit':'Persona de Contacto (Nombre y Apellido):',
            'doc_conv':'Tipo de ID',
            'num_conv':'Número de ID:',
            'apell_conv':'Apellidos',
            'name_conv':'Nombres',
            'vinc_asegur':'VÍNCULO',
            'specif_asegur':'Especifique',
            'doc_asegur':'Tipo de ID',
            'num_asegur':'Número de ID',
            'apell_asegur':'Apellidos',
            'name_asegur':'Nombres',
            'sex_asegur':'Sexo',
            'state_asegur':'Estado Civil',
            'nacim_asegur':'Lugar de Nacimiento',
            'datenacim_asegur':'Fecha de Nacimiento',
            'nacion_asegur':'Nacionalidad',
            'domic_asegur':'Dirección de domicilio',
            'tel_asegur':'Teléfono',
            'mail_asegur':'Email',
            'vinc1_benefic':'VÍNCULO',
            'vinc2_benefic':'Especifique',
            'doc_benefic':'Tipo de ID',
            'num_benefic':'Número de ID',
            'apell_benefic':'Apellidos',
            'name_benefic':'Nombres',
            'sex_benefic':'Sexo',
            'state_benefic':'Estado Civil',
            'nacim_benefic':'Lugar de Nacimiento',
            'datenacim_benefic':'Fecha de Nacimiento',
            'nacion_benefic':'Nacionalidad',
            'domic_benefic':'Dirección de domicilio',
            'tel_benefic':'Teléfono',
            'mail_benefic':'Email',
            #'type_work':'tipo trabajo',
            'especify_work':'Especifique',
            'razon_work':'Nombre o Razón Social  Lugar de trabajo',
            'sector_work':'Sector',
            'activity_work':'Actividad',
            'cargo_work':'Cargo que desempeña',
            'domic_work':'Dirección de trabajo',
            'city_work':'País',
            'ciud_work':'Ciudad',
            'mail_work':'Correo electrónico',
            'tel_work':'teléfono',
            'ingress_info':'Detalle de  ingresos mensuales de actividad declarada:  USD',
            'mesuality_info':'Detalle de  ingresos mensuales USD',
            'other_info':'Fuente de los otros ingresos',
            'activos_info':'Total de Activos',
            'pasivos_info':'Total de Pasivos',
            'patrim_info':'Patrimonio',
            'name_reference':'Nombre y Apellido',
            'parentesc_reference':'Parentesco',
            'tel_reference':'teléfono',
            'target_reference':'Tarjeta',
            'instfin_reference':'Inst. Financiera',
            'ctatype_reference':'Tipo cta. Ahorro /corriente',
            'instbanc_reference':'Inst. Financiera',
            'nameoth_reference':'Nombre y Apellido',
            'parentescoth_reference':'Parentesco',
            'teloth_reference':'teléfono',
            'targetoth_reference':'Tarjeta',
            'instfinoth_reference':'Inst. Financiera',
            'ctatypeoth_reference':'Tipo cta. Ahorro /corriente',
            'instbancoth_reference':'Inst. Financiera',
            #'emision_factur':,
            'social_factur':'Nombre/ Razón social',
            'rucci_factur':'C.I/Ruc No.',
            'tel_factur':'Teléfono',
            'domic_factur':'Dirección',
            'relacion_factur':'Relación con el Solicitante',
            'names_extra':'Nombres y Apellidos',
            #'adicionch_extra':,
            #'specific_extra':'Especifique',
            #'func_extra':'',
            #'canal_extra':,
            #'ced_file':,
            #'serbas_file':,
            #'conv_file':,
            #'cert_file':,
            #'cargo_file':,
            #'renta_file':,
            'lugar_declaration':'Lugar',
            'condic_declaration':'¿Esta de acuerdo con las condiciones?',
        }
        widgets={
            'cliente':
            'tiposeguro':
            'sumasegurada':
            'doc_solicit':
            'num_solicit':
            'apell_solicit':
            'name_solicit':
            'sex_solicit':
            'state_solicit':
            'nacim_solicit':
            'datenacim_solict':
            'nacion_solicit':
            'domic_solict':
            'ciud_solicit':
            'pais_solicit':
            'prov_solicit':
            'tel_solicit':
            'mail_solicit':
            'mail_fact_solicit':
            'mail_form_solicit':
            'contac_solicit':
            'doc_conv':
            'num_conv':
            'apell_conv':
            'name_conv':
            'vinc_asegur':
            'specif_asegur':
            'doc_asegur':
            'num_asegur':
            'apell_asegur':
            'name_asegur':
            'sex_asegur':
            'state_asegur':
            'nacim_asegur':
            'datenacim_asegur':
            'nacion_asegur':
            'domic_asegur':
            'tel_asegur':
            'mail_asegur':
            'vinc1_benefic':
            'vinc2_benefic':
            'doc_benefic':
            'num_benefic':
            'apell_benefic':
            'name_benefic':
            'sex_benefic':
            'state_benefic':
            'nacim_benefic':
            'datenacim_benefic':
            'nacion_benefic':
            'domic_benefic':
            'tel_benefic':
            'mail_benefic':
            'type_work':
            'especify_work':
            'razon_work':
            'sector_work':
            'activity_work':
            'cargo_work':
            'domic_work':
            'city_work':
            'ciud_work':
            'mail_work':
            'tel_work':
            'ingress_info':
            'mesuality_info':
            'other_info':
            'activos_info':
            'pasivos_info':
            'patrim_info':
            'name_reference':
            'parentesc_reference':
            'tel_reference':
            'target_reference':
            'instfin_reference':
            'ctatype_reference':
            'instbanc_reference':
            'nameoth_reference':
            'parentescoth_reference':
            'teloth_reference':
            'targetoth_reference':
            'instfinoth_reference':
            'ctatypeoth_reference':
            'instbancoth_reference':
            'emision_factur':
            'social_factur':
            'rucci_factur':
            'tel_factur':
            'domic_factur':
            'relacion_factur':
            'names_extra':
            'adicionch_extra':
            'specific_extra':
            'func_extra':
            'canal_extra':
            'ced_file':
            'serbas_file':
            'conv_file':
            'cert_file':
            'cargo_file':
            'renta_file':
            'lugar_declaration':
            'condic_declaration':
        }
