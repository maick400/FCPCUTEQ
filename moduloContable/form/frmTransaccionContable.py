from django import forms
from moduloContable.model.model_CNT_Transaccion_Contable import * 
from moduloContable.form.campos import *
from moduloContable.form.choices.estado import *
from moduloContable.form.choices.transaccionContable import *

class frm_Transaccion_Contable(forms.ModelForm):
    class Meta:
        model=Model_CNT_Transaccion_Contable
        fields=(
            DETALLE_TRANSACCION_CONTABLE,
            ESTADO,
            CONT_TIPO_TRANSACCION_CONTABLEID,
        )

        labels={
            DETALLE_TRANSACCION_CONTABLE:"Detalle",
            ESTADO:"Estado",
            CONT_TIPO_TRANSACCION_CONTABLEID:"Tipo Transaccion"
        }


        widgets = {
            DETALLE_TRANSACCION_CONTABLE:forms.TextInput(),
            ESTADO:forms.Select(choices=BOLEANS),
            CONT_TIPO_TRANSACCION_CONTABLEID:forms.Select(choices=TIPO_TRANSACCION_CONTABLE_SELECT)
        }


        help_texts = {

        }

        error_messages = {
            "unique":"transaccion ya registrada"
        }