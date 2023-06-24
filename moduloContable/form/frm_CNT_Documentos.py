from django import forms
from moduloContable.model.model_CNT_Documento import *
from moduloContable.form.choices.choices_documento import *

class Frm_Cnt_Documento(forms.ModelForm):
    
    class Meta:
        model  = Model_CNT_Documentos
        fields=(
            'codigo',
            'documento',
            'origen',
            'prefijo',
            'ultimo_numero',
            'numeracion_automatica',
            'activo',
        )
        labels = {
            'codigo':'Código',
            'documento':'Nombre documento',
            'origen':'Origen',
            'prefijo':'Prefijo',
            'numeracion_automatica':'Numeración automática',
            'activo':'Activo',
        }
        widgets = {
            'codigo':forms.TextInput(),
            'documento':forms.TextInput(),
            'origen':forms.Select(choices=ORIGEN),
            'prefijo':forms.TextInput(),
            'numeracion_automatica':forms.Select(choices=BOOL),
            'activo':forms.Select(choices=BOOL),
        }
        