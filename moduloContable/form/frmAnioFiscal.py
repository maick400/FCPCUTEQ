from django import forms
from moduloContable.model.model_CNT_Anio_Fiscal import * 
from moduloContable.form.choices.anioFiscal import *

class frm_Anio_Fiscal(forms.ModelForm):
    class Meta:
        model=Model_CNT_Anio_Fiscal
        fields=(
            "inicio",
            "fin",
            "activo",
        )

        labels={
            "inicio":"Inicio",
            "fin":"Fin",
            "activo":"Estado",
        }


        widgets = {
            "inicio":forms.DateInput(attrs={"type":"date"}),
            "fin":forms.DateInput(attrs={"type":"date"}),
            "activo":forms.Select(choices=ESTADOC)
        }


        help_texts = {

        }

        error_messages = {
         
        }