from django import forms
from moduloContable.model.mode_SIS_Tipo_Documentos import * 
from moduloContable.form.choices.tipoDocumento import *

class frmTipoDocumentos(forms.ModelForm):
    class Meta:
        model=Model_SIS_Tipo_Documentos
        fields=(
            "nombre",
            "interno_externo",
            "prefijo",
            "ultimo_numero",
            "estado"
        )

        labels={
            "nombre":"Nombre",
            "interno_externo":"Interno Externo",
            "prefijo":"Prefijo",
            "ultimo_numero":"Ultimo numero",
            "estado":"Estado"
        }


        widgets = {
            "nombre":forms.TextInput(),
            "interno_externo":forms.Select(choices=InternoExterno),
            "prefijo":forms.TextInput(),
            "ultimo_numero": forms.NumberInput(),
            "estado": forms.Select(choices=Estado),
        }


        help_texts = {

        }

        error_messages = {
            "nombre":{
                'unique':'Periodo ya existente'
            }
        }