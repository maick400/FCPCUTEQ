from django import forms
from moduloContable.model.model_CNT_Tipo_Transaccion_Contable import * 

class Frm_tipo_Transaccion_Contable(forms.ModelForm):
    class Meta:
        model=Model_CNT_Tipo_Transaccion_Contable
        fields=(
            'tipo_transaccion',
        )

        labels={
            'tipo_transaccion':"Tipo Transaccion",
        }

        widgets = {
            'tipo_transaccion':forms.TextInput(),
        }


        help_texts = {

        }

        error_messages = {
        }