from django import  forms
from moduloFondo.model.Model_FND_tipo_fondo_complementario import Model_FND_tipo_fondo_complementario

#FORMULARIO DE PROVINCIAS
class Frm_Tipo_Fondo_Complementario(forms.ModelForm):
    class Meta:
        model = Model_FND_tipo_fondo_complementario
        fields = (
            'codigo',
            'tipo',
            'descripcion'
        )
        
        
        labels= {
            'codigo': 'Código',
            'tipo': 'Tipo',
            'descripcion': 'Descripción'
        }

        widgets = {
            'codigo': forms.TextInput(),
            'tipo': forms.TextInput(),
            'descripcion': forms.Textarea()
        }
        
        help_texts = {       
        }

        error_messages = {                    
                    'codigo':{
                        'unique':'El código ya existe'
                    }                
                }



