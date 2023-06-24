from django import  forms
from moduloFondo.model.model_FND_socio import Model_FND_socio
from moduloFondo.forms.choices.choices_FND_socios import *

#FORMULARIO DE TIPO DE DESCUENTO
class frm_socio(forms.ModelForm):
    class Meta:
        model = Model_FND_socio
        fields = (
            'genero',
            'estado_civil',
            'direccion',
            'email',
            'fecha_nacimiento',
            'tipo_prestacion',
            'estado',
            'contacto_referencia',
            'total_ahorrado',
            'total_garantizado',
            'foto',
            'total_creditos',
            'id_usuario',
            'pPresta',
        )
        
        labels= {
            'genero': 'Género',
            'estado_civil': 'Estado Civil',
            'direccion': 'Direccion',
            'email': 'Email',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'tipo_prestacion': 'Tipo de Prestación',
            'estado': 'Estado',
            'contacto_referencia': 'Contacto de referencia',
            'total_ahorrado': 'Total Ahorrado',
            'total_garantizado': 'Total Garantizado',
            'foto': 'Foto',
            'total_creditos': 'Total Créditos',
            'id_usuario': 'Usuario',
            'pPresta': 'Presta',
        }

        widgets = {
            'genero' : forms.Select(choices=GENEROS_CHOICES),
            'estado_civil' : forms.Select(choices=ESTADOS_CIVILES_CHOICES),
            'direccion' : forms.TextInput(),
            'email' : forms.EmailInput(),
            'fecha_nacimiento' : forms.DateInput(attrs={'type': 'date'}),
            'tipo_prestacion' : forms.Select(choices=TIPO_PRESTACION_CHOICES),
            'estado' : forms.Select(choices=ESTADO_CHOICES),
            'contacto_referencia' : forms.TextInput(),
            'total_ahorrado' : forms.NumberInput(),
            'total_garantizado' : forms.NumberInput(),
            'foto' : forms.TextInput(),
            'total_creditos' : forms.NumberInput(),
            'id_usuario' : forms.Select(),
            'pPresta' : forms.CheckboxInput(),
        }
        
        help_texts = {

            'direccion':'Ejemplo: Calle 1 # 1-1',
            'email':'Ejemplo: mail@gmail.com',
            'fecha_nacimiento':'Ejemplo: 1990-01-01',
       
        }
        error_messages = {
                    
                    'email':{
                        'unique':'Este correo ya existe'
                    },        
                }



