from django import forms
from moduloContable.model.model_CNT_Asiento_Contable import * 
from moduloContable.form.choices.choices_asientoContable import *
class frmAsiento_Contable(forms.ModelForm):
    class Meta:
        model=Model_Asiento_Contable
        fields=(
        'plantilla',
        'periodo_fiscal',
        'documeto',
        'nombre_documento',
        'numero_documento',
        'transaccion_contable',
        'numero_transaccion',
        'personal',
        'nombre_personal',
        'contador',
        'nombre_contador',
        'gerente',
        'nombre_gerente',
        'presidente',
        'nombre_presidente',
        'fecha_cierre',
        'fecha_mayorización',
        'detalle',
        'descripcion',
        'estado',
        'total_debe',
        'total_haber',
        )
        

        labels={
        'plantilla':'Plantilla',
        'periodo_fiscal':'Periodo Fiscal',
        'documeto':'Documento',
        'nombre_documento':'Nombre del documento',
        'numero_documento': 'N° DOC',
        'transacción' : 'Transacción contable',
        'transaccion_contable':'Nombre trasacción',
        'numero_transaccion':'N° Transacción',
        'personal':'Personal',
        'nombre_personal':'Nombre Personal',
        'contador':'Contador en turno',
        'nombre_contador':'Nombre Contador',
        'gerente':'Gerente en turno',
        'nombre_gerente':'Nombre gerente',
        'presidente':'Presidente',
        'nombre_presidente':'Nombre Presidente',
        'fecha_cierre':'Fecha de cierre',
        'fecha_mayorización':'Fecha mayorización',
        'detalle':'destalle',
        'descripcion':'Descripción',
        'estado':'Estado',
        'total_debe':'Total debe',
        'total_haber':'Total haber',
        }


        widgets = {
        'plantilla':forms.Select(),
        'periodo_fiscal':forms.Select(),
        'documeto':forms.Select(),
        'nombre_documento':forms.TextInput(),
        'numero_documento': forms.Textarea(),
        'transaccion' : forms.Select(),
        'transaccion_contable' : forms.TextInput(),
        'numero_transaccion':forms.TextInput(),
        'personal': forms.Select(),
        'nombre_personal': forms.TextInput(),
        'contador': forms.Select(),
        'nombre_contador':forms.TextInput() ,
        'gerente': forms.Select(),
        'nombre_gerente': forms.TextInput(),
        'presidente': forms.Select(),
        'nombre_presidente': forms.TextInput(),
        'fecha_cierre':forms.DateTimeInput(),
        'fecha_mayorización':forms.DateTimeInput(),
        'detalle': forms.TextInput(),
        'descripcion':forms.Textarea(),
        'estado':forms.Select(choices=ESTADO),
        'total_debe':forms.NumberInput(),
        'total_haber':forms.NumberInput(),
        }


        help_texts = {

        }

        error_messages = {

        }