from django import forms

from moduloCreditos.model.model_CRE_credito_bien import Model_CRE_credito_bien


class frm_credito_bien (forms.ModelForm):
    class Meta:
        model = Model_CRE_credito_bien
        fields= (           
            'id_credito_bien',
            'id_credito_otorgado',
            'bien',
            'avaluo',
            'atributos'
        )

        labels= {
            'id_credito_bien': "Crédito por bien",
            'id_credito_otorgado': "Crédito otorgado",
            'bien': "Bien",
            'avaluo': "Avaluo",
            'atributos': "Atributos del bien"
        }


        widgets = {
            'id_credito_bien': forms.Select(attrs={'class': 'form-select'}),
            'id_credito_otorgado': forms.Select(attrs={'class': 'form-select'}),
            'bien': forms.TextInput(),
            'avaluo': forms.NumberInput(),
            'atributos': forms.Textarea()
        }

        help_texts = {

        }

        error_messages = {
           
        }