from django import  forms
from moduloFondo.model.model_FND_parametros_sys import Model_FND_Parametros_sys
from moduloFondo.forms.choices.choices_FND_parametros_sys import *

#FORMULARIO DE PARAMETROS DEL SISTEMA
class frm_parametros_sys(forms.ModelForm):
    class Meta:
        model = Model_FND_Parametros_sys
        fields = (
            'nombre_fondo',
            'nombre_contador',
            'matricula_contador',
            'cedula_rep_legal',
            'nombre_rep_legal',
            'ced_representante_Creditos',
            'nombre_rep_credito',
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
            'nombre_contador': 'Nombre del Contador',
            'matricula_contador': 'Matricula del Contador',
            'cedula_rep_legal': 'Cedula del Representante Legal',
            'nombre_rep_legal': 'Nombre del Representante Legal',
            'ced_representante_Creditos': 'Cedula del Representante de Creditos',
            'nombre_rep_credito': 'Nombre del Representante de Creditos',
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
            'nombre_contador': forms.TextInput(attrs={'class': 'form-control'}),
            'matricula_contador': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula_rep_legal': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_rep_legal': forms.TextInput(attrs={'class': 'form-control'}),
            'ced_representante_Creditos': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_rep_credito': forms.TextInput(attrs={'class': 'form-control'}),
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
            'nombre_contador': 'Ingrese el nombre del contador',
            'matricula_contador': 'Ingrese la matricula del contador',
            'cedula_rep_legal': 'Ingrese la cedula del representante legal',
            'nombre_rep_legal': 'Ingrese el nombre del representante legal',
            'ced_representante_Creditos': 'Ingrese la cedula del representante de creditos',
            'nombre_rep_credito': 'Ingrese el nombre del representante de creditos',
            'fecha_const_fondo': 'Ingrese la fecha de constitucion del fondo',
            'correo': 'Ingrese el correo electronico',
            'smtp_server': 'Ingrese el servidor SMTP',
            'smtp_port': 'Ingrese el puerto SMTP',
            'smtp_cuenta': 'Ingrese la cuenta SMTP',
            'smtp_password': 'Ingrese la contraseña SMTP',
            'tipo_aportaciion': 'Seleccione el tipo de aportacion',
            'valor_aplicable_aportación': 'Ingrese el valor aplicable a la aportación',
        }
        
