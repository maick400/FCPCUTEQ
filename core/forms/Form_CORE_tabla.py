from django import  forms
from core.model.Model_CORE_tabla import Model_CORE_tabla

#FORMULARIO DE TABLA
class Form_CORE_tabla(forms.ModelForm):
    class Meta:
        model = Model_CORE_tabla
        fields = (           
            'nombre_tabla',
            'numero_tabla',
            'ente_provee_tabla',            
            'descripcion'
        )
        
        labels= {
            'nombre_tabla': 'Tabla',
            'numero_tabla': 'Número de tabla',
            'ente_provee_tabla': 'Entidad proveedora',            
            'descripcion': 'Descripción'
        }

        widgets = {
            'nombre_tabla': forms.TextInput(),
            'numero_tabla': forms.NumberInput(),
            'ente_provee_tabla': forms.TextInput(),            
            'descripcion': forms.Textarea()
        }
        
        help_texts = {
            'nombre_tabla': 'Ingrese el nombre de la tabla',
            'numero_tabla': 'Ingrese el número que representa la tabla',
        }

        error_messages = {          
        }