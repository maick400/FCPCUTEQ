from django import  forms
from moduloFondo.model.model_FND_Personal  import *


class Frm_FDN_Personal (forms.ModelForm):
    class Meta:
        model = Model_FND_Personal
        
        fields  = ('__all__');
        
        widgets = {
            'nombres':forms.TextInput(),
            'apellido_paterno':forms.Textarea(),
            'apellido_materno':forms.Textarea(),
            'sexo':forms.Select(),
            'foto':forms.FilePathField(),
            'tipo_identificacion':forms.Select(),
            'identificación':forms.TextInput(),
            'pais':forms.Select(),
            'direccion':forms.Textarea(),
            'activo':forms.Select()
        }
    