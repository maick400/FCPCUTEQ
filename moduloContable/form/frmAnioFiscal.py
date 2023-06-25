from django import forms
from moduloContable.model.model_CNT_Anio_Fiscal import * 
from moduloContable.form.choices.choices_anio_fiscal import *

class Frm_Anio_Fiscal(forms.ModelForm):
    class Meta:
        model=Model_CNT_Anio_Fiscal
        fields=(
            'anio',
            'inicio',
            'fin',
            'estado',
        )

        labels={
            'anio':'Año Fiscal',
            'inicio':"Fecha Inicio",
            'fin':"Fecha Fin",
            'estado':"Estado",
        }


        widgets = {
            
            'anio':forms.NumberInput(attrs={"type":"date"}),
            'inicio':forms.DateInput(attrs={"type":"date"}),
            'fin':forms.DateInput(attrs={"type":"date"}),
            'estado':forms.Select(choices=ESTADO),
        }


        help_texts = {

        }

        error_messages = {
         
        }