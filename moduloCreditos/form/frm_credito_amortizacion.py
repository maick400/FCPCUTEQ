from django import forms

from moduloCreditos.model.model_CRE_credito_amortizacion import Model_CRE_credito_amortizacion
from moduloCreditos.form.campos import *

class frm_credito_amortizacion(forms.ModelForm):
    class Meta:
        model = Model_CRE_credito_amortizacion
        fields= (           
            'id_credito_otorgado',
            'numero_cuota',
            'fecha_pago',
            'pago_capital',
            'pago_interes',
            'seguro_desgravamen',
            'cuota_total',
            'saldo_actual',
            'dias_vencidos'
        )

        labels={        
            'id_credito_otorgado': 'Credito otorgado',
            'numero_cuota': 'Número de cuota',
            'fecha_pago': 'Fecha de pago',
            'pago_capital': 'Pago capital',
            'pago_interes': 'Pago interes',
            'seguro_desgravamen': 'Seguro de desgravamen',
            'cuota_total': 'Cuota total',
            'saldo_actual': 'Saldo actual',
            'dias_vencidos': 'Días vencidos'
        }


        widgets = {
            'id_credito_otorgado': forms.Select(attrs={'class': 'form-select'}),
            'numero_cuota': forms.NumberInput(),
            'fecha_pago': forms.DateTimeInput(attrs={'type': 'date'}),
            'pago_capital': forms.NumberInput(),
            'pago_interes': forms.NumberInput(),
            'seguro_desgravamen': forms.NumberInput(),
            'cuota_total': forms.NumberInput(),
            'saldo_actual': forms.NumberInput(),
            'dias_vencidos': forms.NumberInput()
        }

        help_texts = {

        }

        error_messages = {
           
        }