from django import forms
from moduloCreditos.model.model_CRE_tipo_credito import Model_CRE_tipo_credito


class frm_tipo_credito (forms.ModelForm):
    class Meta:
        model = Model_CRE_tipo_credito
        fields = (
   
            'tipo_credito',
            'porc_ahorro_acceso',
            'valor_maximo',
            'max_credito_anios',
            'prioridad_calif_cartera',
            'tipo_garan_calif_cartera',
            'permite_garante',
            'gerencia_requerida',
            'genera_amortizacion',
            'activo',
            'fecha_creacion',
            'fecha_modificacion'
        )

        labels = {
           
            'tipo_credito': "Tipo credito",
            'porc_ahorro_acceso': "Porcentaje ahorro acceso",
            'valor_maximo': "Valor maximo",
            'max_credito_anios': "Maximo credito anios",
            'prioridad_calif_cartera': "Prioridad calificacion cartera",
            'tipo_garan_calif_cartera': "Tipo garante calificacion cartera",
            'permite_garante': "Permite garante",
            'gerencia_requerida': "Gerencia requerida",
            'genera_amortizacion': "Genera amortizacion",
            'activo': "Activo",
            'fecha_creacion': "Fecha creacion",
            'fecha_modificacion': "Fecha modificacion"
        }
        
        widgets = {
            'tipo_credito': forms.TextInput(),
            'porc_ahorro_acceso': forms.NumberInput(),
            'valor_maximo': forms.NumberInput(),
            'max_credito_anios': forms.NumberInput(),
            'prioridad_calif_cartera': forms.NumberInput(),
            'tipo_garan_calif_cartera': forms.TextInput(),
            'permite_garante': forms.CheckboxInput(),
            'gerencia_requerida': forms.CheckboxInput(),
            'genera_amortizacion': forms.CheckboxInput(),
            'activo': forms.CheckboxInput(),
            'fecha_creacion': forms.DateTimeInput(attrs={'type': 'date'}),
            'fecha_modificacion': forms.DateTimeInput(attrs={'type': 'date'}),
        }