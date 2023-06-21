from django import forms
from moduloContable.model.model_CNT_Anio_Fiscal import * 
from moduloContable.form.campos import *
from moduloContable.form.choices.estado import *

class frm_Anio_Fiscal(forms.ModelForm):
    class Meta:
        model=Model_CNT_Anio_Fiscal
        fields=(
            INICIO_ANIO_FISCAL,
            FIN_ANIO_FISCAL,
            ESTADO,
        )

        labels={
            INICIO_ANIO_FISCAL:"Inicio",
            FIN_ANIO_FISCAL:"Fin",
            ESTADO:"Estado",
        }


        widgets = {
            INICIO_ANIO_FISCAL:forms.DateInput(attrs={"type":"date"}),
            FIN_ANIO_FISCAL:forms.DateInput(attrs={"type":"date"}),
            ESTADO:forms.Select(choices=BOLEANS)
        }


        help_texts = {

        }

        error_messages = {
         
        }