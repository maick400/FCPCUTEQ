from django.urls import path
from moduloCreditos.views import *

app_name = 'creditos'
 
urlpatterns = [
    path( 'tipo_credito/crear/', crear_tipo_credito, name='crear_tipo_credito'),
    path( 'tipo_credito/listar/', listar_tipo_credito, name='listar_tipo_credito'),
    
    path( 'tipo_bien/crear/', crear_tipo_bien, name='crear_tipo_bien'),
    path( 'tipo_bien/listar/', listar_tipo_bien, name='listar_tipo_bien'),


    path( 'tipo_creditos_atributo/crear/', crear_tipo_bien_atributo, name='crear_tipo_bien_atributo'),
    path( 'tipo_creditos_atributo/listar/', listar_tipo_bien_atributo, name='listar_tipo_bien_atributo'),

    path( 'tipo_bien_tipo_credito/crear/', crear_tipo_bien_tipo_credito, name='crear_tipo_bien_tipo_credito'),
    #Arreglar, ruta no válida
    path( 'solicitud_credito_bien/crear/', crear_credito_bien_solicitud, name='crear_credito_bien_solicitud'),
    path( 'tipo_creditos_docs_requeridos/crear/', crear_doc_requerido_credito, name='crear_doc_requerido_credito'),
    path( 'tipo_bien_documentos/crear/', crear_tipo_bien_documento, name='crear_tipo_bien_documento'),
    path( 'solicitud_credito/crear/', crear_solicitud_credito, name='crear_solicitud_credito'),
    path( 'solicitud_credito/listar/', listar_solicitud_credito, name='listar_solicitud_credito'),
    
    path( 'solicitud_bien/crear/', crear_solicitud_bienes, name='crear_solicitud_bienes'),
    path( 'solicitud_documentos_bien/crear/', crear_solicitud_documento_bien, name='crear_solicitud_documento_bien'),
    
    path( 'credito_amortizacion/crear/', crear_tabla_amortizacion, name='crear_tabla_amortizacion'),
    path( 'credito_amortizacion/listar/', listar_tabla_amortizacion, name='listar_tabla_amortizacion'),

    path( 'credito_pagos/crear/', crear_pago_credito, name='crear_pago_credito'),
    path( 'credito_pagos/listar/', listar_pago_credito, name='listar_pago_credito'),


    path( 'credito_bien/crear/', crear_credito_bien, name='crear_credito_bien'),
    path( 'credito_bien/listar/', listar_credito_bien, name='listar_credito_bien'),
    
    path( 'credito_garante/crear/', crear_credito_garante, name='crer_credito_garante'),
    path( 'credito_garante/listar/', listar_credito_garante, name='listar_credito_garante')
]   
 