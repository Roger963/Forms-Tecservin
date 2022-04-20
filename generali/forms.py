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
        city_choices = (('AFG','AFGANISTAN'),('AX','ALAND'),('AL','ALBANIA'),('DEU','ALEMANIA'),('AD','ANDORRA'),('AO','ANGOLA'),('AI','ANGUILA'),('AQ','ANTARTIDA'),('AG','ANTIGUA Y BARBUDA'),
            ('AN','ANTILLAS NEERLANDESAS'),('SA','ARABIA SAUDITA'),('DZ','ARGELIA'),('ARP','ARGENTINA'),('AM','ARMENIA'),('AW','ARUBA'),('AUD','AUSTRALIA'),('AT','AUSTRIA'),('AZ','AZERBAIYAN'),
            ('BS','BAHAMAS'),('BH','BAHREIN'),('BB','BARBADOS'),('BLR','BELARAUS'),('BE','BELGICA'),('BZ','BELICE'),('BJ','BENIN'),('BM','BERMUDAS'),('BY','BIELORRUSIA'),('MMR','BIRMANIA'),
            ('BOL','BOLIVIA'),('BA','BOSNIA Y HERZEGOVINA'),('BW','BOTSUANA'),('BRC','BRASIL'),('BN','BRUNEI'),('BG','BULGARIA'),('BF','BURKINA FASO'),('BDI','BURUNDI'),('BT','BUTAN'),
            ('CV','CABO VERDE'),('KH','CAMBOYA'),('CM','CAMERUN'),('CAD','CANADA'),('TD','CHAD'),('CLP','CHILE'),('CHN','CHINA'),('CY','CHIPRE'),('VA','CIUDAD DEL VATICANO'),('COP','COLOMBIA'),
            ('KM','COMORAS'),('PRK','COREA DEL NORTE'),('KR','COREA DEL SUR'),('CIV','COSTA DE MARFIL'),('CR','CRIMEA'),('HR','CROACIA'),('CUP','CUBA'),('DKK','DINAMARCA'),('DM','DOMINICA'),
            ('ECS','ECUADOR'),('EG','EGIPTO'),('SV','EL SALVADOR'),('AE','EMIRATOS ARABES UNIDOS'),('ERI','ERITREA'),('SK','ESLOVAQUIA'),('SI','ESLOVENIA'),('ESP','ESPA¥A'),('USA','ESTADOS UNIDOS'),
            ('EE','ESTONIA'),('ET','ETIOPIA'),('PH','FILIPINAS'),('FI','FINLANDIA'),('FJ','FIYI'),('FRP','FRANCIA'),('GA','GABON'),('GM','GAMBIA'),('GE','GEORGIA'),('GH','GHANA'),('GD','GRANADA'),
            ('GR','GRECIA'),('GL','GROENLANDIA'),('GP','GUADALUPE'),('GU','GUAM'),('GTQ','GUATEMALA'),('GF','GUAYANA FRANCESA'),('GG','GUERNSEY'),('GIN','GUINE'),('GQ','GUINEA ECUATORIAL'),
            ('GNB','GUINEA-BISSAU'),('GY','GUYANA'),('HTI','HAITI'),('NLG','HOLANDA'),('HN','HONDURAS'),('HK','HONG KONG'),('HU','HUNGRIA'),('IN','INDIA'),('ID','INDONESIA'),('ING','INGLATERRA'),
            ('IRR','IRAN'),('IRQ','IRAQ'),('IE','IRLANDA'),('BV','ISLA BOUVET'),('IM','ISLA DE MAN'),('CX','ISLA DE NAVIDAD'),('IS','ISLANDIA'),('KY','ISLAS CAIMáN'),('CC','ISLAS COCOS'),
            ('CK','ISLAS COOK'),('FO','ISLAS FEROE'),('GS','ISLAS GEORGIAS DEL SUR Y SANDWICH DEL SUR'),('HM','ISLAS HEARD Y MCDONALD'),('FK','ISLAS MALVINAS'),('MP','ISLAS MARIANAS DEL NORTE'),
            ('MH','ISLAS MARSHALL'),('PN','ISLAS PITCAIRN'),('SB','ISLAS SALOMON'),('TC','ISLAS TURCAS Y CAICOS'),('UM','ISLAS ULTRAMARINAS DE ESTADOS UNIDOS'),('VG','ISLAS VIRGENES BRITANICAS'),
            ('VI','ISLAS VIRGENES ESTADOUNIDENSES'),('IL','ISRAEL'),('ITA','ITALIA'),('JM','JAMAICA'),('JP','JAPON'),('JE','JERSEY'),('JO','JORDANIA'),('KZ','KAZAJISTAN'),('KE','KENIA'),
            ('KG','KIRGUISTAN'),('KI','KIRIBATI'),('KW','KUWAIT'),('LA','LAOS'),('LS','LESOTO'),('LV','LETONIA'),('LBN','LIBANO'),('LR','LIBERIA'),('LBY','LIBIA'),('LI','LIECHTENSTEIN'),('LT','LITUANIA'),
            ('LU','LUXEMBURGO'),('MO','MACAO'),('MK','MACEDONIA'),('MG','MADAGASCAR'),('MY','MALASIA'),('MW','MALAUI'),('MV','MALDIVAS'),('MLI','MALI'),('MT','MALTA'),('MA','MARRUECOS'),
            ('MQ','MARTINICA'),('MU','MAURICIO'),('MR','MAURITANIA'),('YT','MAYOTTE'),('MXP','MEXICO'),('FM','MICRONESIA'),('MD','MOLDAVIA'),('MC','MONACO'),('MN','MONGOLIA'),('ME','MONTENEGRO'),
            ('MS','MONTSERRAT'),('MZ','MOZAMBIQUE'),('MMR','MYANMAR'),('NA','NAMIBIA'),('NR','NAURU'),('NP','NEPAL'),('NIC','NICARAGUA'),('NE','NIGER'),('NG','NIGERIA'),('NU','NIUE'),('NF','NORFOLK'),
            ('NO','NORUEGA'),('NC','NUEVA CALEDONIA'),('NZ','NUEVA ZELANDA'),('OM','OMAN'),('NLD','PAISES BAJOS'),('PAK','PAKISTAN'),('PW','PALAOS'),('PAB','PANAMA'),('PG','PAPUA NUEVA GUINEA'),
            ('PY','PARAGUAY'),('PES','PERU'),('PF','POLINESIA FRANCESA'),('PL','POLONIA'),('PT','PORTUGAL'),('QA','QATAR'),('GBR','REINO UNIDO'),('COD','REP.DEMOCRATICA DEL CONGLO'),
            ('CAF','REPUBLICA CENTROAFRICANA'),('CF','REPUBLICA CENTROAFRICANA'),('CZ','REPúBLICA CHECA'),('CG','REPUBLICA DEL CONGO'),('CD','REPUBLICA DEMOCRATICA'),('DO','REPUBLICA DOMINICANA'),
            ('RE','REUNION'),('RW','RUANDA'),('ROS','RUMANIA'),('RUS','RUSIA'),('EH','SAHARA OCCIDENTAL'),('AS','SAMOA AMERICANA'),('BL','SAN BARTOLOMé'),('KN','SAN CRISTOBAL Y NIEVES'),('SM','SAN MARINO'),
            ('PM','SAN PEDRO Y MIQUELON'),('VC','SAN VICENTE Y LAS GRANADINAS'),('SH','SANTA HELENA'),('LC','SANTA LUCIA'),('ST','SANTO TOME Y PRINCIPE'),('SN','SENEGAL'),('RS','SERBIA'),
            ('SC','SEYCHELLES'),('SL','SIERRA LEONA'),('SG','SINGAPUR'),('SYR','SIRIA'),('SOM','SOMALIA'),('SSD','SOUTH SUDAN'),('LK','SRI LANKA'),('SZ','SUAZILANDIA'),('ZA','SUDAFRICA'),
            ('SDN','SUDAN'),('SEK','SUECIA'),('CHF','SUIZA'),('SR','SURINAM'),('SJ','SVALBARD Y JAN MAYEN'),('TH','TAILANDIA'),('TW','TAIWAN'),('TZ','TANZANIA'),('TJ','TAYIKISTAN'),
            ('IO','TERRITORIO BRITáNICO DEL OCéANO ÍNDICO'),('TF','TERRITORIOS AUSTRALES FRANCESES'),('PS','TERRITORIOS PALESTINOS'),('TL','TIMOR ORIENTAL'),('TG','TOGO'),('TK','TOKELAU'),('TO','TONGA'),
            ('TT','TRINIDAD Y TOBAGO'),('TN','TUNEZ'),('TM','TURKMENISTAN'),('TR','TURQUIA'),('TV','TUVALU'),('UKR','UCRANIA'),('UG','UGANDA'),('EU','UNION EUROPEA'),('SU','UNION SOVIETICA'),
            ('UZ','URBEKISTAN'),('UYP','URUGUAY'),('VU','VANUATU'),('VEB','VENEZUELA'),('VN','VIETNAM'),('WF','WALLIS Y FUTUNA'),('YEM','YEMEN'),('DJ','YIBUTI'),('ZM','ZAMBIA'),('ZWE','ZIMBABUE'),)
        MEDIA_CHOICES = [
            ('Audio', (
                    ('vinyl', 'Vinyl'),
                    ('cd', 'CD'),
                )
            ),
            ('Video', (
                    ('vhs', 'VHS Tape'),
                    ('dvd', 'DVD'),
                ) 
            ),
            ('unknown', 'Unknown'),
        ]
        
        model = Formulario
        fields = '__all__'
        widgets={
            'cliente': forms.Select(choices=MEDIA_CHOICES),
            'tiposeguro': forms.Select(choices=ramo_choices),
            'sumasegurada': forms.TextInput(),
        }
