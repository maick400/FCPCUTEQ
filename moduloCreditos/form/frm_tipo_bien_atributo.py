from django import forms

from moduloCreditos.model.model_CRE_tipo_bien_atributo import Model_CRE_tipo_bien_atributo
from moduloCreditos.form.campos import *

class frm_tipo_bien_atributo(forms.ModelForm):
    class Meta:
        model = Model_CRE_tipo_bien_atributo
        fields= (       
            ID_TIPO_BIEN,   
            ATRIBUTO,
            TIPO_DATO,
            OBLIGATORIO
        )

        labels={
            ID_TIPO_BIEN: "Bien",
            ATRIBUTO: "Atributo",
            TIPO_DATO: "Tipo de dato",
            OBLIGATORIO: "Obligatorio"
        }


        widgets = {
            ID_TIPO_BIEN: forms.Select(),
            ATRIBUTO: forms.TextInput(),
            TIPO_DATO: forms.TextInput(),
            OBLIGATORIO: forms.CheckboxInput()
        }

        help_texts = {

        }

        error_messages = {
            ATRIBUTO: {
                'unique':'El atributo ya está registrado'
            }
        }