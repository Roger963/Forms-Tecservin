from django.forms import ModelForm
from django import forms
from .models import Formulario

class FormularioForm(ModelForm):
    cliente = forms.TextInput()
    tiposeguro = forms.TextInput()
    
    class Meta:
        model = Formulario
        fields = '__all__'
        labels ={
            'cliente': 'Client',
            'tiposeguro': 'Tip',
            'sumasegurada': 'Suma asegurada',
            'doc_solicit': 'Solicitante',
        }
        widgets={
            'cliente': forms.RadioSelect(),
            'tiposeguro': forms.RadioSelect(),
            'sumasegurada': forms.TextInput(attrs={'class': 'form-control'}),
            'doc_solicit': forms.TextInput(attrs={'class': 'form-control'}),
        }