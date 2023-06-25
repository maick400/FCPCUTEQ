from django import forms

from moduloCreditos.model.model_CRE_solicitud_credito import Model_CRE_solicitud_credito

class frm_solicitud_credito(forms.ModelForm):
    class Meta:
        model = Model_CRE_solicitud_credito
        fields= (           
            #'id_fondo_socio',
            'id_tipo_credito',
            #'id_personal_recibido',
            #'id_personal_validado',
            'monto',
            'numero_cuotas',
            'tasa_interes'
        )

        labels={
            #'id_fondo_socio': 'Socio',
            'id_tipo_credito': 'Tipo de crédito',
            #'id_personal_recibido': 'Receptor',
            #'id_personal_validado': 'Validador',
            'monto': 'Monto',
            'numero_cuotas': 'Número de cuotas',
            'tasa_interes': 'Tasa de interes'
        }


        widgets = {
            #'id_fondo_socio': forms.Select(),
            'id_tipo_credito': forms.Select(),
            #'id_personal_recibido': forms.Select(),
            #'id_personal_validado': forms.Select(),
            'monto': forms.NumberInput(),
            'numero_cuotas': forms.NumberInput(),
            'tasa_interes': forms.NumberInput()
        }

        help_texts = {

        }

        error_messages = {
           
        }