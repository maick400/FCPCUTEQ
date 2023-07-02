from django.urls import path
from moduloFondo.forms import *
from moduloFondo.views import *
from moduloFondo.vw_casanova import *
from moduloFondo.vw_pina import *
from moduloFondo.vw_jhon import *
from moduloFondo.vw_ochoa import *



app_name = 'fondo'
urlpatterns = [
    
    path('operadora/registrar/', crear_operadora_telefonica, name='crear_operadora_telefonica'),
    path('operadora/listar/', listar_operadora_telefonica, name='listar_operadora_telefonica'),
    path('operadora/editar/<pk>', editar_operadora_telefonica, name='editar_operadora_telefonica'),
    path('operadora/buscar/', buscar_operadora, name='buscar_operadora'),
    
    #*----------------------RUTAS SOCIO----------------------#
    path('socio/registrar/', crear_socio, name='crear_socio'),
    path('socio/lista/', listar_socio, name='listar_socio'),
    path('socio/editar/<pk>/', editar_socio, name='editar_socio'),
    path('socio/buscar/', buscar_socio, name='buscar_socio'),
    #----------------------RUTAS SOCIO----------------------#

    # * ----------------------RUTAS PROVINCIAS----------------------#
    path('provincias/lista/', listar_provincias, name='listar_provincias'),
    path('provincias/registrar/', agregar_provincia, name='agregar_provincia'),
    path('provincias/editar/<pk>', editar_provincia, name='editar_provincia'),
    path('provincias/buscar/', buscar_provincia, name='buscar_provincia'),
    # *----------------------RUTAS PROVINCIAS----------------------#

    path('canton/listar/', listar_canton, name='listar_cantones'),
    path('canton/registrar/', agregar_canton, name='agregar_canton'),
    path('canton/editar/<pk>', editar_canton, name='editar_canton'),
    path('canton/buscar/', buscar_canton, name='buscar_canton'),
    
    # *----------------------RUTAS TIPO FONDO----------------------#
    path('tipo_fondo/registrar/', crear_tipo_fondo, name='crear_tipo_fondo'),
    path('tipo_fondo/listar', listar_tipo_fondo, name='listar_tipo_fondo'),
    path('tipo_fondo/editar/<pk>/', editar_tipo_fondo, name='editar_tipo_fondo'),
    path('tipo_fondo/buscar', buscar_tipo_fondo, name='buscar_tipo_fondo'),
    
    # TODO----------------------RUTAS TIPO FONDO----------------------#
    path('solicitudes_generales/registrar/', crear_solicitudes_generales, name='crear_solicitudes_generales'),
    path('solicitudes_generales/listar', listar_solicitudes_generales, name='listar_solicitud_general'),
    path('solicitudes_generales/editar/<pk>/', editar_solicitudes_generales, name='editar_solicitud_general'),
    path('solicitudes_generales/buscar', buscar_solicitud, name='buscar_solicitud_generales'),
    # TODO----------------------RUTAS TIPO FONDO----------------------#

    path('modulos/registrar/', predeterminado, name='crear_tipo_fondo'),
    path('modulos/listar', predeterminado, name='listar_tipo_fondo'),
    path('modulos/editar/<pk>/', predeterminado, name='editar_tipo_fondo'),
    path('modulos/buscar', predeterminado, name='buscar_tipo_fondo'),
]
    
