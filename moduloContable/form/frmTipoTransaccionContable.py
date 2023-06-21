from django import forms
from moduloContable.model.model_CNT_Tipo_Transaccion_Contable import * 
from moduloContable.form.campos import *
from moduloContable.form.choices.estado import *

class frm_tipo_Transaccion_Contable(forms.ModelForm):
    class Meta:
        model=Model_CNT_Tipo_Transaccion_Contable
        fields=(
            TIPO_TRANSACCION,
        )

        labels={
            TIPO_TRANSACCION:"Tipo Transaccion",
        }


        widgets = {
            TIPO_TRANSACCION:forms.TextInput(),
        }


        help_texts = {

        }

        error_messages = {
            "unique":"Tipo transaccion ya registrada"
        }