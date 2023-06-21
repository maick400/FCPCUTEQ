from django import forms

from moduloCreditos.model.model_CRE_tipo_bien import Model_CRE_tipo_bien
from moduloCreditos.form.campos import *

class frm_tipo_bien(forms.ModelForm):
    class Meta:
        model = Model_CRE_tipo_bien
        fields= (           
            NOMBRE_BIEN,
            AVALUO,
            OBSERVACION
        )

        labels={
            NOMBRE_BIEN: "Bien",
            AVALUO: "Avaluo",
            OBSERVACION: "Observación"
        }


        widgets = {
            NOMBRE_BIEN: forms.TextInput(),
            AVALUO: forms.NumberInput(),
            OBSERVACION: forms.Textarea()
        }

        help_texts = {

        }

        error_messages = {
            NOMBRE_BIEN:{
                'unique':'El bien ya está registrado'
            }
        }