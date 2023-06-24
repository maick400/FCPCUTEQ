from django import forms

from moduloCreditos.model.model_CRE_tipo_credito_docs_requeridos import Model_CRE_tipo_credito_docs_requeridos
from moduloCreditos.form.campos import *

class frm_tipo_credito_docs_requeridos(forms.ModelForm):
    class Meta:
        model = Model_CRE_tipo_credito_docs_requeridos
        fields= (           
           'id_tipo_credito',
           'nombre_documento',
           'es_requerido'
        )

        labels={
            'id_tipo_credito': "Credito",
            'nombre_documento': "Documento requerido",
            'es_requerido': "Requerido"         
        }


        widgets = {
            'id_tipo_credito':forms.Select(),
            'nombre_documento': forms.TextInput(),
            'es_requerido': forms.CheckboxInput()
        }

        help_texts = {

        }

        error_messages = {
            'nombre_documento': {
                'unique':'El documento ya está registrado'
            }
        }