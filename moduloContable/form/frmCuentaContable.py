from django import forms
from moduloContable.model.model_CNT_Cuenta_Contable import * 
from moduloContable.form.choices.choices_cuentaContable import *
class frm_crear_cuenta_contable(forms.ModelForm):
    class Meta:
        model=Model_CNT_Cuenta_Contable
        fields=(
            'codigo_cuenta',
            'cuenta_padre',
            'nombre_cuenta',
            'naturaleza',
            'movimiento_mayor',
            'nivel',
            'cuc_reg',
            'activa',
        )

        labels={
            'codigo_cuenta':'Código',
            'cuenta_padre':'Cuenta Padre',
            'nombre_cuenta':'Cuenta',
            'naturaleza':'Naturaleza',
            'movimiento_mayor':'Mayor/Menor',
            'nivel':'Nivel',
            'cuc_reg':'CUC SB',
            'activa':'Activa',
        }


        widgets = { 
            'codigo_cuenta':forms.TextInput(),
            'cuenta_padre':forms.Select(),
            'nombre_cuenta':forms.TextInput(),
            'naturaleza':forms.Select(choices=NATURALEZA),
            'movimiento_mayor':forms.Select(choices=MAYOR_MENOR),
            'nivel':forms.Select(choices=NIVEL),
            'cuc_reg':forms.Select(choices=BOOL),
            'activa':forms.Select(choices=BOOL)
        }


        help_texts = {
        }

        error_messages = {
 
        }