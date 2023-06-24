from django import forms
from moduloContable.model.model_CNT_Transaccion_Contable import * 
from moduloContable.form.choices.transaccionContable import *

class frm_Transaccion_Contable(forms.ModelForm):
    class Meta:
        model=Model_CNT_Transaccion_Contable
        fields=(
            "detalle",
            "estado",
            "id_tipo_transaccion",
        )

        labels={
            "detalle":"Detalle",
            "estado":"Estado",
            "id_tipo_transaccion":"Tipo Transaccion"
        }


        widgets = {
            "detalle":forms.TextInput(),
            "estado":forms.Select(choices=ESTADOC),
            "id_tipo_transaccion":forms.Select()
        }


        help_texts = {

        }

        error_messages = {
            "unique":"transaccion ya registrada"
        }