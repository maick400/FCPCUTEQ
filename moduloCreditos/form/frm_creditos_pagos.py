from django import forms

from moduloCreditos.model.model_CRE_credito_pagos import Model_CRE_credito_pagos
from moduloCreditos.form.campos import *

class frm_creditos_pagos(forms.ModelForm):
    class Meta:
        model = Model_CRE_credito_pagos
        fields= (           
            'id_credito_otorgado',
            'fecha_cancelacion',
            'numero_cuota',
            'pago_interes',            
        )

        labels={        
            'id_credito_otorgado': 'Crédito otorgado',
            'fecha_cancelacion': 'Fecha de cancelación',
            'numero_cuota': "Número de cuotas",
            'pago_interes': "Pago de interes"
        }


        widgets = {
            'id_credito_otorgado': forms.Select(attrs={'class': 'form-select'}),
            'fecha_cancelacion': forms.DateTimeInput(attrs={'type': 'date'}),            
            'numero_cuota': forms.NumberInput(),
            'pago_interes': forms.NumberInput()
        }

        help_texts = {

        }

        error_messages = {
           
        }