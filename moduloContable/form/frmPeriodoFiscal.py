from django import forms
from moduloContable.model.model_CNT_Periodo_Fiscal import * 
from moduloContable.form.choices.choices_periodo_fiscal import *

class Frm_Periodo_Fiscal(forms.ModelForm):
    class Meta:
        model=Model_CNT_Periodo_Fiscal
        fields=(
            'anio_fiscal',
            'numero',
            'nombre',
            'inicio',
            'fin',
            'estado',
        )

        labels={
            'anio_fiscal':'Año fiscal',
            'numero':'Número',
            'nombre':'Nombre',
            'inicio':'Fecha inicio',
            'fin':'Fecha fin',
            'estado':'Estado',
        }


        widgets = {
            'anio_fiscal':forms.Select(),
            'numero':forms.NumberInput(),
            'nombre':forms.TextInput(),
            'inicio':forms.DateInput(attrs={"type":"date"}),
            'fin':forms.DateInput(attrs={"type":"date"}),
            'estado':forms.Select(choices=ESTADO),
        }


        help_texts = {

        }

        error_messages = {
        }