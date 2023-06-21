from django import forms
from moduloContable.model.model_CNT_Asiento_Contable import * 
from moduloContable.form.choices.asientoContable import *
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
            "transaccion_contable",
            "descripcion",
            "documento",
            "numero_documento",
            "nombre_persona1",
            "nombre_representante",
            "total_debe",
            "total_haber",
            "balance",
            "bit"
        )

        labels={
            #NOMBRE_CUENTA_AC:"Nombre Cuenta",
            #DETALLE:"Naturaleza",
            #DEBE:"Movimiento Mayor",
            #HABER:"Nivel",
            #PERIODO_FISCAL:"Cuc Reg",
            #TIPO_DOCUMENTO:"Estado",
            "transaccion_contable":"Transaccion Contable",
            "descripcion":"Descripcion",
            "documento":"Documento",
            "numero_documento":"Numero Documento",
            "nombre_persona1":"Nombre Persona",
            "nombre_representante":"Nombre Representante",
            "total_debe":"Total Debe",
            "total_haber":"Total Haber",
            "balance":"Balance",
            "bit":"Estado"
        }


        widgets = {
            #NOMBRE_CUENTA_AC:forms.Select(choices=NOMBRE_CUENTA_SELECT),
            #DETALLE:forms.TextInput(),
            #DEBE:forms.TextInput(),
            #HABER:forms.TextInput(),
            #PERIODO_FISCAL:forms.Select(choices=NOMBRE_CUENTA_SELECT),
            #TIPO_DOCUMENTO:forms.Select(choices=TIPO_DOCUMENTO_SELECT),
            "transaccion_contable":forms.Select(choices=TRANSACCION_CONTABLE_SELECT),
            "descripcion":forms.TextInput(),
            "documento":forms.FileInput(),
            "numero_documento":forms.TextInput(),
            "nombre_persona1":forms.TextInput(),
            "nombre_representante":forms.TextInput(),
            "total_debe":forms.TextInput(),
            "total_haber":forms.TextInput(),
            "balance":forms.TextInput(),
            "bit":forms.Select(choices=BOLEANS),
        }


        help_texts = {

        }

        error_messages = {
            "nombre_cuenta":{
                'unique':''
            }
        }