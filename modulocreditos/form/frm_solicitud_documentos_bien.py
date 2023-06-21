from django import forms

from moduloCreditos.model.model_CRE_solicitud_documentos_bien import Model_CRE_solicitud_documentos_bien

class frm_solicitud_documentos_bien(forms.ModelForm):
    class Meta:
        model = Model_CRE_solicitud_documentos_bien
        fields= (                      
            'id_solicitud_bien',
            'nombre_documento',
            'ruta_documento',          
        )

        labels={            
            'id_solicitud_bien': 'Solicitud',
            'nombre_documento': 'Título del documento',
            'ruta_documento': 'Documento',            
        }


        widgets = {
            'id_solicitud_bien': forms.TextInput(),
            'nombre_documento': forms.TextInput(),
            'ruta_documento': forms.TextInput(),           
        }

        help_texts = {

        }

        error_messages = {
           
        }