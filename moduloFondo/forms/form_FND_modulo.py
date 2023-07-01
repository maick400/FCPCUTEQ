from django import  forms
from moduloFondo.model.model_FND_modulo import Model_FND_modulo

#FORMULARIO DE PROVINCIAS
class Frm_Modulo(forms.ModelForm):
    class Meta:
        model = Model_FND_modulo

        #exclude = ['id_modulo']
        
        fields = (
            '__all__'
        )                

        widgets = {
            'nombre_modulo': forms.TextInput(),
            'app_label': forms.TextInput(),
            'url_modulo': forms.TextInput(),
            #'foto_modulo_ruta': forms.FileInput(attrs={'class': 'form-control'}),
            'foto_modulo_ruta': forms.FileInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(),
            'activo': forms.CheckboxInput(),
            'fecha_creacion': forms.DateTimeField(),
            'fecha_modificacion': forms.DateTimeField()
        }
        
        help_texts = {       
        }

        error_messages = {            
            'nombre_modulo':{
                'unique':'El nombre del módulo ya existe'
            },
        }



