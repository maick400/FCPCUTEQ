from django import  forms
from moduloFondo.model.model_FND_parametros_sys import Model_FND_Parametros_sys
from moduloFondo.model.choices.choices_FND_parametros_sys import *

#FORMULARIO DE PARAMETROS DEL SISTEMA
class frm_parametros_sys(forms.ModelForm):
    class Meta:
        model = Model_FND_Parametros_sys
        fields = (
            'nombre_fondo',
            'contador',
            'matricula_contador',
            'representante_legal',
            'responsable_creditos',
            'fecha_const_fondo',
            'correo',
            'smtp_server',
            'smtp_port',
            'smtp_cuenta',
            'smtp_password',
            'tipo_aportaciion',
            'valor_aplicable_aportación',
        )
        labels = {
            'nombre_fondo': 'Nombre del Fondo',
            'contador': 'Nombre del Contador',
            'matricula_contador': 'Matricula del Contador',
            'representante_legal': 'Nombre del Representante Legal',
            'responsable_creditos': 'Nombre del Representante de Creditos',
            'fecha_const_fondo': 'Fecha de Constitucion del Fondo',
            'correo': 'Correo Electronico',
            'smtp_server': 'Servidor SMTP',
            'smtp_port': 'Puerto SMTP',
            'smtp_cuenta': 'Cuenta SMTP',
            'smtp_password': 'Contraseña SMTP',
            'tipo_aportaciion': 'Tipo de Aportacion',
            'valor_aplicable_aportación': 'Valor Aplicable Aportación',
        }
        widgets = {
            'nombre_fondo': forms.TextInput(attrs={'class': 'form-control'}),
            'contador': forms.TextInput(attrs={'class': 'form-control'}),
            'matricula_contador': forms.TextInput(attrs={'class': 'form-control'}),
            'representante_legal': forms.TextInput(attrs={'class': 'form-control'}),
            'responsable_creditos': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_const_fondo': forms.DateInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'smtp_server': forms.TextInput(attrs={'class': 'form-control'}),
            'smtp_port': forms.NumberInput(attrs={'class': 'form-control'}),
            'smtp_cuenta': forms.NumberInput(attrs={'class': 'form-control'}),
            'smtp_password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'tipo_aportaciion': forms.Select(choices=TIPO_APORTACION, attrs={'class': 'form-control'}),
            'valor_aplicable_aportación': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'nombre_fondo': 'Ingrese el nombre del fondo',
            'contador': 'Ingrese el nombre del contador',
            'matricula_contador': 'Ingrese la matricula del contador',
            'representante_legal': 'Ingrese el nombre del representante legal',
            'responsable_creditos': 'Ingrese el nombre del representante de creditos',
            'fecha_const_fondo': 'Ingrese la fecha de constitucion del fondo',
            'correo': 'Ingrese el correo electronico',
            'smtp_server': 'Ingrese el servidor SMTP',
            'smtp_port': 'Ingrese el puerto SMTP',
            'smtp_cuenta': 'Ingrese la cuenta SMTP',
            'smtp_password': 'Ingrese la contraseña SMTP',
            'tipo_aportaciion': 'Seleccione el tipo de aportacion',
            'valor_aplicable_aportación': 'Ingrese el valor aplicable a la aportación',
        }
        
