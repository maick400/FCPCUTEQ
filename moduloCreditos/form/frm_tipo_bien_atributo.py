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
            OBLIGATORIO,
            'fecha_creacion',
            'fecha_modificacion',
        )

        labels={
            ID_TIPO_BIEN: "Bien",
            ATRIBUTO: "Atributo",
            TIPO_DATO: "Tipo de dato",
            OBLIGATORIO: "Obligatorio",
            'fecha_creacion': "Fecha de creación",
            'fecha_modificacion': "Fecha de modificación",

        }


        widgets = {
            ID_TIPO_BIEN: forms.Select(),
            ATRIBUTO: forms.TextInput(),
            TIPO_DATO: forms.TextInput(),
            OBLIGATORIO: forms.CheckboxInput(),
            'fecha_creacion': forms.DateInput(),
            'fecha_modificacion': forms.DateInput(),
        }

        help_texts = {

        }

        error_messages = {
            ATRIBUTO: {
                'unique':'El atributo ya está registrado'
            }
        }