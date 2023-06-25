from django import forms

from moduloCreditos.model.model_CRE_credito_bien_solicitud import Model_CRE_credito_bien_solicitud
from moduloCreditos.form.campos import *

class frm_credito_bien_solicitud(forms.ModelForm):
    class Meta:
        model = Model_CRE_credito_bien_solicitud
        fields= (           
            'id_credito_bien',
            'nombre_documento',
            'ruta_documento'
        )

        labels={
            'id_credito_bien': "Bien",
            'nombre_documento': "Título del documento",
            'ruta_documento': "Documento"
        }


        widgets = {
            'id_credito_bien': forms.TextInput(),
            'nombre_documento': forms.TextInput(),
            'ruta_documento': forms.FileInput()
        }

        help_texts = {

        }

        error_messages = {
           
        }