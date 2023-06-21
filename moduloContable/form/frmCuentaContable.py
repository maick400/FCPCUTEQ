from django import forms
from moduloContable.model.model_CNT_Cuenta_Contable import * 
from moduloContable.form.choices.cuentaContable import *
from moduloContable.form.choices.estado import *

class frm_crear_cuenta_contable(forms.ModelForm):
    class Meta:
        model=Model_CNT_Cuenta_Contable
        fields=(
            "nombre_cuenta",
            "naturaleza",
            "movimiento_mayor",
            "nivel",
            "cuc_reg",
            "estado"
        )

        labels={
            "nombre_cuenta":"Nombre Cuenta",
            "naturaleza":"Naturaleza",
            "movimiento_mayor":"Movimiento Mayor",
            "nivel":"Nivel",
            "cuc_reg":"Cuc Reg",
            "estado":"Estado"
        }


        widgets = {
            "nombre_cuenta":forms.TextInput(),
            "naturaleza":forms.Select(choices=NATURALEZA),
            "movimiento_mayor":forms.Select(choices=MAYOR_MOVIMIENTO),
            "nivel":forms.Select(choices=NIVEL),
            "cuc_reg":forms.TextInput(),
            "estado":forms.Select(choices=BOLEANS)
        }


        help_texts = {
             "nombre_cuenta":'Ejemplo: Cajas',
        }

        error_messages = {
            "nombre_cuenta":{
                'unique':'Esta cuenta ya ha sido registrada'
            }
        }