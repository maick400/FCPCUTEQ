from django import  forms
from core.model.Model_CORE_valores import Model_CORE_valores

#FORMULARIO DE VALORES
class Form_CORE_valores(forms.ModelForm):
    class Meta:
        model = Model_CORE_valores
        fields = (                                
           'id_campo',
           'valor',
           'activo'
        )
        
        labels= { 
           'id_campo': 'Campo',
           'valor': 'Valor',
           'activo': 'Activo'     
        }

        widgets = {
            'id_campo': forms.Select(),
            'valor': forms.TextInput(),
            'activo': forms.Select()
        }
        
        help_texts = {
            'id_campo': 'Ingrese el campo relacionado al valor',
            'valor': 'Ingrese el nombre del valor'
        }

        error_messages = {          
        }