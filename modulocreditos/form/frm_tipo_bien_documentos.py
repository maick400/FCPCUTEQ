from django import forms

from moduloCreditos.model.model_CRE_tipo_bien_documento import Model_CRE_tipo_bien_documento

class frm_tipo_bien_documento(forms.ModelForm):
    class Meta:
        model = Model_CRE_tipo_bien_documento
        fields= (           
            'id_tipo_bien',
            'nombre_documento',
        )

        labels={
            'id_tipo_bien': "Bien",
            'nombre_documento': "Título del documento",
        }


        widgets = {
            'id_tipo_bien': forms.Select(),
            'nombre_documento': forms.TextInput(),
        }

        help_texts = {

        }

        error_messages = {
           
        }