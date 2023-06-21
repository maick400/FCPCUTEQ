from django import forms
from moduloContable.model.model_CNT_Cuenta_Contable import * 
from moduloContable.form.choices.cuentaContable import *
from moduloContable.form.campos import *
from moduloContable.form.choices.estado import *

class frm_crear_cuenta_contable(forms.ModelForm):
    class Meta:
        model=Model_CNT_Cuenta_Contable
        fields=(
            NOMBRE_CUENTA_CONTABLE,
            NATURALEZA_CONTABLE,
            MOVIMIENTO_MAYOR_CONTABLE,
            NIVEL_CONTABLE,
            CUC_REG_CONTABLE,
            ESTADO
        )

        labels={
            NOMBRE_CUENTA_CONTABLE:"Nombre Cuenta",
            NATURALEZA_CONTABLE:"Naturaleza",
            MOVIMIENTO_MAYOR_CONTABLE:"Movimiento Mayor",
            NIVEL_CONTABLE:"Nivel",
            CUC_REG_CONTABLE:"Cuc Reg",
            ESTADO:"Estado"
        }


        widgets = {
            NOMBRE_CUENTA_CONTABLE:forms.TextInput(),
            NATURALEZA_CONTABLE:forms.Select(choices=NATURALEZA),
            MOVIMIENTO_MAYOR_CONTABLE:forms.Select(choices=MAYOR_MOVIMIENTO),
            NIVEL_CONTABLE:forms.Select(choices=NIVEL),
            CUC_REG_CONTABLE:forms.TextInput(),
            ESTADO:forms.Select(choices=BOLEANS)
        }


        help_texts = {
             NOMBRE_CUENTA_CONTABLE:'Ejemplo: Cajas',
        }

        error_messages = {
            NOMBRE_CUENTA_CONTABLE:{
                'unique':'Esta cuenta ya ha sido registrada'
            }
        }