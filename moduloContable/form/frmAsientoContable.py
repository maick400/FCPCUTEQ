from django import forms
from moduloContable.model.model_CNT_Asiento_Contable import * 
from moduloContable.form.choices.asientoContable import *
from moduloContable.form.campos import *
from moduloContable.form.choices.estado import *

class frmAsiento_Contable(forms.ModelForm):
    class Meta:
        model=Model_Asiento_Contable
        fields=(
            #NOMBRE_CUENTA_AC,
            #DETALLE,
            #DEBE,
            #HABER,
            #PERIODO_FISCAL,
            #TIPO_DOCUMENTO,
            TRANSACCION_CONTABLE,
            DESCRIPCION,
            DOCUMENTO,
            NUMERO_DOCUMENTO,
            NOMBRE_PERSONA,
            NOMBRE_REPRESENTANTE,
            TOTAL_DEBE,
            TOTAL_HABER,
            BALANCE,
            SYSTEM
        )

        labels={
            #NOMBRE_CUENTA_AC:"Nombre Cuenta",
            #DETALLE:"Naturaleza",
            #DEBE:"Movimiento Mayor",
            #HABER:"Nivel",
            #PERIODO_FISCAL:"Cuc Reg",
            #TIPO_DOCUMENTO:"Estado",
            TRANSACCION_CONTABLE:"Transaccion Contable",
            DESCRIPCION:"Descripcion",
            DOCUMENTO:"Documento",
            NUMERO_DOCUMENTO:"Numero Documento",
            NOMBRE_PERSONA:"Nombre Persona",
            NOMBRE_REPRESENTANTE:"Nombre Representante",
            TOTAL_DEBE:"Total Debe",
            TOTAL_HABER:"Total Haber",
            BALANCE:"Balance",
            SYSTEM:"Estado"
        }


        widgets = {
            #NOMBRE_CUENTA_AC:forms.Select(choices=NOMBRE_CUENTA_SELECT),
            #DETALLE:forms.TextInput(),
            #DEBE:forms.TextInput(),
            #HABER:forms.TextInput(),
            #PERIODO_FISCAL:forms.Select(choices=NOMBRE_CUENTA_SELECT),
            #TIPO_DOCUMENTO:forms.Select(choices=TIPO_DOCUMENTO_SELECT),
            TRANSACCION_CONTABLE:forms.Select(choices=TRANSACCION_CONTABLE_SELECT),
            DESCRIPCION:forms.TextInput(),
            DOCUMENTO:forms.FileInput(),
            NUMERO_DOCUMENTO:forms.TextInput(),
            NOMBRE_PERSONA:forms.TextInput(),
            NOMBRE_REPRESENTANTE:forms.TextInput(),
            TOTAL_DEBE:forms.TextInput(),
            TOTAL_HABER:forms.TextInput(),
            BALANCE:forms.TextInput(),
            SYSTEM:forms.Select(choices=BOLEANS),
        }


        help_texts = {

        }

        error_messages = {
            NOMBRE_CUENTA_AC:{
                'unique':''
            }
        }