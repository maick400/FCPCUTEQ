from django import  forms
from moduloFondo.model.model_FND_socio import Model_FND_socio
from django.contrib.auth.models import User
from moduloFondo.model.model_FND_provincia import Model_FND_provincia



from datetime import datetime
#FORMULARIO DE TIPO DE DESCUENTO
class frm_socio(forms.ModelForm):
    class Meta:
        model = Model_FND_socio
        exclude = ['id_socio']
        fields = ('__all__')
            
        

        widgets = {
            'id_usuario': forms.Select(),
            'id_provincia': forms.Select(),
            'nombres': forms.TextInput(),
            'apellido_paterno': forms.TextInput(),
            'apellido_materno': forms.TextInput(),
            'genero': forms.Select(),
            'tipo_identificacion': forms.Select(),
            'identificacion': forms.TextInput(),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'estado_civil': forms.Select(),
            'pais': forms.Select(),
            'ciudad': forms.TextInput(),
            'direccion': forms.TextInput(),
            'foto_ruta': forms.FileInput(attrs={'class': 'form-control'}),
            'total_ahorrado': forms.NumberInput(),
            'total_garantizado': forms.NumberInput(),
            'total_monto_creditos_vigente': forms.NumberInput(),
            'numero_aportaciones': forms.NumberInput(),
            'numero_aportaciones_consecutivas': forms.NumberInput(),
            'estado_participe': forms.Select(),
            'tipo_sistema': forms.Select(),
            'base_calculo_aportacion': forms.Select(),
            'tipo_relacion': forms.Select(),
            'estado_registro': forms.Select(),
            'fecha_creacion': forms.HiddenInput(),
            'fecha_modificacion': forms.HiddenInput(),
        }
    
        help_texts = {

            'id_usuario': 'Seleccione el usuario',
            'id_provincia': 'Seleccione la provincia',
            'nombres': 'Ingrese los nombres',
            'apellido_paterno': 'Ingrese el apellido paterno',
            'apellido_materno': 'Ingrese el apellido materno',
            'genero': 'Seleccione el género',
            'tipo_identificacion': 'Ingrese el tipo de identificación',
            'identificacion': 'Ingrese la identificación',
            'fecha_nacimiento': 'Ingrese la fecha de nacimiento',
            'estado_civil': 'Seleccione el estado civil',
            'pais': 'Seleccione el país',
            'ciudad': 'Ingrese la ciudad',
            'direccion': 'Ingrese la dirección',
            'foto_ruta': 'Suba la foto',
            'total_ahorrado': 'Ingrese el total ahorrado',
            'total_garantizado': 'Ingrese el total garantizado',
            'total_monto_creditos_vigente': 'Ingrese el monto de créditos vigentes',
            'numero_aportaciones': 'Ingrese el número de aportaciones',
            'numero_aportaciones_consecutivas': 'Ingrese el número de aportaciones consecutivas',
            'estado_participe': 'Seleccione el estado partícipe',
            'tipo_sistema': 'Seleccione el tipo de sistema',
            'base_calculo_aportacion': 'Seleccione la base de cálculo de aportación',
            'tipo_relacion': 'Seleccione el tipo de relación',
            'estado_registro': 'Ingrese el estado de registro',

       
        }
        error_messages = {
                    
                    'identificacion': {'unique': ("La identificación ya existe.")},     
                }


