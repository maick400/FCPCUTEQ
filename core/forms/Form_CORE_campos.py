from django import  forms
from core.model.Model_CORE_campos import Model_CORE_campos

#FORMULARIO DE CAMPOS
class Form_CORE_campos(forms.ModelForm):
    class Meta:
        model = Model_CORE_campos
        fields = (                      
            'id_tabla',
            'nombre_campo'
        )
        
        labels= {          
            'id_tabla': 'Tabla',
            'nombre_campo': 'Campo'
        }

        widgets = {
            'id_tabla': forms.Select(),
            'nombre_campo': forms.TextInput()
        }
        
        help_texts = {
            'id_tabla': 'Ingrese la tabla relacionada',
            'nombre_campo': 'Ingrese el nombre del campo'
        }

        error_messages = {          
        }