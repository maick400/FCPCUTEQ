from django import forms
from moduloContable.model.model_CNT_Periodo_Fiscal import * 
from moduloContable.form.campos import *
from moduloContable.form.choices.estado import *

class frmPeriodo_Fiscal(forms.ModelForm):
    class Meta:
        model=Model_CNT_Periodo_Fiscal
        fields=(
            NOMBRE_PERIODO_FISCAL,
            INICIO_PERIODO_FISCAL,
            FIN_PERIODO_FISCAL,
            ESTADO
        )

        labels={
            NOMBRE_PERIODO_FISCAL:"Nombre",
            INICIO_PERIODO_FISCAL:"Inicio",
            FIN_PERIODO_FISCAL:"Fin",
            ESTADO:"estado",
        }


        widgets = {
            NOMBRE_PERIODO_FISCAL:forms.TextInput(),
            INICIO_PERIODO_FISCAL:forms.DateInput(attrs={"type":"date"}),
            FIN_PERIODO_FISCAL:forms.DateInput(attrs={"type":"date"}),
            ESTADO:forms.Select(choices=BOLEANS)
        }


        help_texts = {

        }

        error_messages = {
            NOMBRE_PERIODO_FISCAL:{
                'unique':'Periodo ya existente'
            }
        }