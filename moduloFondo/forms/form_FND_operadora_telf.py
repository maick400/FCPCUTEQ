from django import  forms
from moduloFondo.model.model_FND_operadora_telf import Model_FND_operadora_telf

#FORMULARIO DE CARGO DE EMPLEADO
class frm_operadora(forms.ModelForm):
    class Meta:
        model = Model_FND_operadora_telf
        fields = (
            'operadora',
        )
        
        labels= {
            'operadora': 'Operadora',
        }

        widgets = {
            'operadora' : forms.TextInput(),
        }
        
        help_texts = {
            'operadora' : 'Ingrese la operadora del teléfono',
        }

        error_messages = {
            'cargo' : {
                'max_length' : 'La operadora no puede tener más de 20 caracteres',
                'required' : 'La operadora es requerido',
                'unique' : 'La operadora ya existe',
            },
        }