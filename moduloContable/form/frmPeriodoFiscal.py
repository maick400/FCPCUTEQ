from django import forms
from moduloContable.model.model_CNT_Periodo_Fiscal import * 
from moduloContable.form.choices.PeriodoFiscal import *

class frmPeriodo_Fiscal(forms.ModelForm):
    class Meta:
        model=Model_CNT_Periodo_Fiscal
        fields=(
            "nombre",
            "inicio",
            "fin",
            "estado"
        )

        labels={
            "nombre":"Nombre",
            "inicio":"Inicio",
            "fin":"Fin",
            "estado":"estado",
        }


        widgets = {
            "nombre":forms.TextInput(),
            "inicio":forms.DateInput(attrs={"type":"date"}),
            "fin":forms.DateInput(attrs={"type":"date"}),
            "estado":forms.Select(choices=ESTADOC)
        }


        help_texts = {

        }

        error_messages = {
            "nombre":{
                'unique':'Periodo ya existente'
            }
        }