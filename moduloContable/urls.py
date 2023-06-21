from django.urls import path 
from moduloContable.views import * 

app_name = 'moduloContable'

urlpatterns = [
    # cuentas contables 
    #path('cuentas_contables/', cuentas_contable_inicio, name='cuentas_contable_inicio' ),
    path('anio_fiscal/crear/', anio_contable, name='anio_fiscal_crear' ),
    path('periodo_fiscal/crear/', periodo_Fiscal, name='periodo_fiscal_crear'),
    path('cuentas_contables/crear/', cuentas_contables, name='cuentas_contable_crear'),
    path('asiento_contable/crear/', asiento_contable, name='asiento_contable_crear'),
    path('tipo_transaccion_contable/crear/', tipoTransaccion, name='tipo_transaccion_contable_crear'),
    path('transaccion_contable/', transaccionContable, name='transaccion_contable'),
    path('tipo_documento/crear/', tipoDocumento, name='tipo_documento_crear'),
]
