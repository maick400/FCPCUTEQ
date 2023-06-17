from django.urls import path 
from moduloContable.views import * 

app_name = 'moduloContable'

urlpatterns = [
    # cuentas contables 
    path('cuentas_contables/', cuentas_contable_inicio, name='cuentas_contable_inicio' ),
    path('cuentas_contables/crear/', cuentas_contable_crear, name='cuentas_contable_crear' )
]
