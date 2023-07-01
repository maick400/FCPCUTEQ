from django import forms
from moduloFondo.model.model_CORE_parametros_sys import * 

class Frm_Fnd_Parametros_Sys(forms.ModelForm):
    class Meta:
        model = Model_FND_Parametros_sys
        
        fields =  (
           
            'provincia',

        )
        
        labels = {

            'provincia':'Provincia',
           
            
        }
        
        widgets = {
            'provincia':forms.Select(),
        }