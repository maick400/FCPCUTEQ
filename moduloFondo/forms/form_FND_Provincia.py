from django import  forms
from moduloFondo.model.Model_FND_provincia import Model_FND_provincia

#FORMULARIO DE PROVINCIAS
class Frm_Provincia(forms.ModelForm):
    class Meta:
        model = Model_FND_provincia
        fields = (
            'codigo',
            'provincia',
        )
        
        
        labels= {
            'codigo': 'Código de provincia',
            'provincia': 'Provincia'
        }

        widgets = {
            'codigo':forms.TextInput(),
            'provincia' : forms.TextInput()     
        }
        
        help_texts = {       
        }

        error_messages = {                  
            'codigo':{
                'unique':'El código ya existe'
            },      
            'provincia':{
                'unique':'La provincia ya existe'
            }      
        }



