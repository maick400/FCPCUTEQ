from django import forms
from moduloContable.model.model_CNT_Asiento_Contable import * 
from moduloContable.form.choices.asientoContable import *
from moduloContable.form.choices.estado import *
import datetime

class frmAsiento_Contable(forms.ModelForm):
    class Meta:
        model=Model_Asiento_Contable
        fields=(
            'CONT_Diario_PlantillaID',
            'periodo_fiscal',
            'Sis_Tipo_DocumentosCodigo',
            'id_transaccion_contable',
            'transaccion_contable',
            'numero_transaccion',
            'fecha_emision',
            'descripcion',
            'documento',
            'numero_documento',
            'nombre_persona1',
            'estado',
            'nombre_representante',
            'total_debe',
            'total_haber',
            'balance',
            'estado',
        )

        labels={
            'CONT_Diario_PlantillaID':'Plantilla',
            'periodo_fiscal':'Periodo_Fiscal',
            'Sis_Tipo_DocumentosCodigo':'Documento',
            'id_transaccion_contable':'transaccion',
            'transaccion_contable':'Transacción',
            'numero_transaccion':'N° Transacción',
            'fecha_emision':'Fecha',
            'descripcion':'Descripción',
            'documento':'Documento',
            'numero_documento': 'N° Documento',
            'nombre_persona1':'Personal',
            'nombre_representante':'Representante actual',
            'total_debe': 'Total debe',
            'total_haber':'Total haber',
            'balance':'Balance',
            'estado':'Estado',
        }
        
        widgets = {
            'CONT_Diario_PlantillaID':forms.Select(),
            'periodo_fiscal':forms.Select(),
            'Sis_Tipo_DocumentosCodigo':forms.Select(),
            'id_transaccion_contable': forms.Select(),
            'transaccion_contable':forms.TextInput(attrs={'disabled':'True'}),
            'numero_transaccion':forms.NumberInput(attrs={'disabled':'True'}),
            'fecha_emision':forms.TextInput(attrs={'value':datetime.datetime.now, 'disabled':'True'}),
            'descripcion':forms.TextInput(),
            'documento':forms.TextInput(attrs={'disabled':'false'}),
            'numero_documento': forms.TextInput(),
            'nombre_persona1':forms.TextInput(attrs={'disabled':'True'}),
            'nombre_representante':forms.TextInput(),
            'total_debe': forms.NumberInput(attrs={'disabled':'True'}),
            'total_haber':forms.NumberInput(attrs={'disabled':'True'}),
            'balance':forms.NumberInput(attrs={'disabled':'True'}),
            'estado':forms.TextInput(attrs={'disabled':'True'}),
        }


        help_texts = {

        }

        error_messages = {
            "nombre_cuenta":{
                'unique':''
            }
        }