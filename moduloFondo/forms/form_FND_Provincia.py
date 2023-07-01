from django import  forms
from moduloFondo.model.model_FND_provincia import Model_FND_provincia

#FORMULARIO DE PROVINCIAS
class Frm_Provincia(forms.ModelForm):
    class Meta:
        model = Model_FND_provincia
        fields = (
            '__all__'
        )        
        
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


urls_provincia = {
            'crear': 'fondo/provincia/provincia_crear.html',
            'editar': 'fondo/provincia/provincia_editar.html',
            'listar': 'fondo/provincia/provincia_listar.html',
            'buscar': 'fondo/provincia/provincia_buscar.html'
        }