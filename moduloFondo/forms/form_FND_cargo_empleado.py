from django import  forms
from moduloFondo.model.model_FND_empleado_cargo import Model_FND_Empleado_Cargo

#FORMULARIO DE CARGO DE EMPLEADO
class frm_cargo_empleado(forms.ModelForm):
    class Meta:
        model = Model_FND_Empleado_Cargo
        fields = (
            'cargo',
        )
        
        labels= {
            'cargo': 'Cargo',
        }

        widgets = {
            'cargo' : forms.TextInput(),
        }
        
        help_texts = {
            'cargo' : 'Ingrese el cargo del empleado',
        }

        error_messages = {
            'cargo' : {
                'max_length' : 'El cargo no puede tener más de 50 caracteres',
                'required' : 'El cargo es requerido',
                'unique' : 'El cargo ya existe',
            },
        }