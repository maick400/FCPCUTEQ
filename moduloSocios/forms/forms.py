from django.urls import reverse_lazy
from django import  forms
from moduloSocios.models import Socio
from moduloSocios.choises import * 

class frm_crear_socio(forms.ModelForm):   
    class Meta: 
        model = Socio
        fields = (
            'cedula',
            'nombres',
            'genero',
            'estado_civil',
            'direccion',
            'fecha_nacimiento',
            'telefono',
            'celular',
            'email',
        ) 
        
        labels= {
            'cedula': 'Cédula',
            'nombres' : 'Nombres',
            'genero' : 'Género',
            'estado_civil' : 'Estado civil',
            'direccion' : 'Dirección',
            'fecha_nacimiento' : 'Fecha de nacimiento',
            'telefono' : 'Teléfono',
            'celular':'Celular',
            'email' : 'Email',
        }

        widgets = {
            'cedula' : forms.TextInput(),
            'nombres' : forms.TextInput(),
            'genero' : forms.Select(choices=GENEROS),
            'estado_civil' : forms.Select(choices=ESTADOS_CIVILES),
            'direccion' : forms.Textarea(),
            'fecha_nacimiento' : forms.DateInput(attrs={'type':'date'}),
            'telefono' : forms.TextInput(),
            'celular' : forms.TextInput(),
            'email' : forms.TextInput(),
            
        }
        
        help_texts = {
            'cedula':'Ejemplo: 1411000001',
            'email':'Ejemplo: masasd@asdas.com',

        }
        
        error_messages = {
            
            'email':{
                'unique':'Este correo ya existe'
            },
            'cedula':{
                
            },
        
        }
        
class Frm_filtros_busqueda(forms.ModelForm):
    class Meta: 
        model = Socio
        fields = (
            'cedula',
        ) 

        labels = {
            'cedula':'Cedula/Nombres'
        }
        
        widgets = {
            'cedula' : forms.TextInput(attrs={
                'hx-post':reverse_lazy('socio:buscar_socio'),
                'hx-trigger':'keyup changed delay:200ms',
                'hx-target':'#resultados-busqueda-socios',
                'name':'general'
                }),
            
        }
        
        
        
        
        
        
        
        