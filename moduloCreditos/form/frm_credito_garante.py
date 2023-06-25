from django import forms
from django.db import connection

from moduloCreditos.form.choices.test import *

from moduloCreditos.model.model_CRE_credito_garante import Model_CRE_credito_garante


class frm_credito_garante (forms.ModelForm):
    
    
    class Meta:
        model = Model_CRE_credito_garante
        fields= (           
            'id_solicitud_credito',
            'id_credito_otorgado',
            #'id_socio',
            'saldo_credito_actual',
            'genero'
        )

        labels= {
            'id_solicitud_credito': "Solicitud de crédito",
            'id_credito_otorgado': "Crédito otorgado",
            #'id_socio': "Socio",
            'saldo_credito_actual': "Crédito actual",
            'genero': "Género"
        }


        widgets = {
            'id_solicitud_credito': forms.Select(attrs={'class':'form-select'}),
            #'id_solicitud_credito': forms.Select(attrs={'class':'form-select'}),
            'id_credito_otorgado': forms.Select(attrs={'class':'form-select'}),
            
            'id_credito_otorgado': forms.Select(attrs={'class':'form-select'}),            
            #'id_socio': "Socio",
            'saldo_credito_actual': forms.NumberInput(),
            'genero': get_values("Select * from obtener_datos_funcion(2)"),
        }

        help_texts = {

        }

        error_messages = {
           
        }