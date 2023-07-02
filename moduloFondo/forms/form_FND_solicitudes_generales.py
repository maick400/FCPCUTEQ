from django import forms
from moduloFondo.model.model_FND_solicitudes_generales import *
from moduloFondo.model.choices.choices_FND_solicitudes_generales import *


class frm_Fnd_solicitudes_generales(forms.ModelForm):
    class Meta:
        model = Model_FND_solicitudes_generales
        fields=('__all__')
        


        widgets = {
            'documento': forms.TextInput(),
            'plantilla_solicitud_ruta': forms.FileInput(attrs={'class': 'form-control'}),
            'descripcion':forms.Textarea(),
            'activo':forms.CheckboxInput()
        }