from django import  forms
from moduloFondo.model.model_FND_canton import Model_FND_canton

#FORMULARIO DE PROVINCIAS
class Frm_Canton(forms.ModelForm):
    class Meta:
        model = Model_FND_canton
        fields = (
            'codigo',
            'cod_provincia',
            'canton'
        )
        
        
        labels= {
            'codigo': 'Código',
            'cod_provincia': 'Provincia',
            'canton': 'Cantón'
        }

        widgets = {
            'codigo': forms.TextInput(),
            'cod_provincia': forms.Select(),
            'canton': forms.TextInput()
        }
        
        help_texts = {       
        }

        error_messages = {
                    
                    'codigo':{
                        'unique':'El código ya existe'
                    },  
                     'canton':{
                        'unique':'El cantón ya existe'
                    },        
                }



