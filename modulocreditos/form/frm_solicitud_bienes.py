from django import forms

from moduloCreditos.model.model_CRE_solicitud_bien import Model_CRE_solicitud_bien

class frm_solicitud_bienes(forms.ModelForm):
    class Meta:
        model = Model_CRE_solicitud_bien
        fields= (                      
            'id_solicitud_credito',
            'avaluo',
            'bien',
            'estado',
            'atributo'
        )

        labels={            
            'id_solicitud_credito': 'Monto',
            'avaluo': 'Número de cuotas',
            'bien': 'Tasa de interes',
            'estado': "Estado",
            'atributo': "Atributos"
        }


        widgets = {
            'id_solicitud_credito': forms.NumberInput(),
            'avaluo': forms.NumberInput(),
            'bien': forms.NumberInput(),
            'estado': forms.Select(),
            'atributo': forms.Textarea()
        }

        help_texts = {

        }

        error_messages = {
           
        }