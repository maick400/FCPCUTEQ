from django import  forms
from moduloFondo.model.model_FND_tipo_descuento import Model_FND_tipo_descuento
#from moduloFondo.forms.choices.choices_FND_tipo_descuento import choices_FND_tipo_descuento

#FORMULARIO DE CREAR TIPO DE DESCUENTO
class frm_tipo_descuento(forms.ModelForm):
    class Meta:
        model = Model_FND_tipo_descuento
        fields = (
            'tipo_descuento',
            'descuento',
        )
        
        labels= {
            'tipo_descuento': 'Tipo de descuento',
            'descuento' : 'Descuento',
        }

        widgets = {
            'tipo_descuento' : forms.TextInput(),
            'descuento' : forms.TextInput(),
        }
        
        help_texts = {
            'tipo_descuento':'Ejemplo: 1411000001',
            'descuento':'Ejemplo: '}
        


