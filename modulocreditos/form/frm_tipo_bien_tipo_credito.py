from django import forms

from moduloCreditos.model.model_CRE_tipo_bien_tipo_credito import Model_CRE_tipo_bien_tipo_credito
from moduloCreditos.form.campos import *

class frm_tipo_bien_tipo_credito(forms.ModelForm):
    class Meta:
        model = Model_CRE_tipo_bien_tipo_credito
        fields= (           
           ID_TIPO_CREDITO,
           ID_TIPO_BIEN,
           ESTADO
        )

        labels={
            ID_TIPO_CREDITO: "Credito",
            ID_TIPO_BIEN: "Bien",
            ESTADO: "Estado"            
        }


        widgets = {
            ID_TIPO_CREDITO: forms.Select(),
            ID_TIPO_BIEN: forms.Select(),
            ESTADO: forms.CheckboxInput()
        }

        help_texts = {

        }

        error_messages = {
            ESTADO: {
                'unique':''
            }
        }