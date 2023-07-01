from django.urls import path
from moduloFondo.forms import *
from moduloFondo.views import *
from moduloFondo.vw_casanova import *
from moduloFondo.vw_pina import *
from moduloFondo.vw_jhon import *
from moduloFondo.vw_ochoa import *



app_name = 'fondo'
urlpatterns = [
    
    path('operadora/registrar/', crear_operadora_telefonica, name='crear_operadora_telefonica'), #type:ignore    
    path('operadora/listar/', listar_operadora_telefonica, name='listar_operadora_telefonica'),
    path('operadora/editar/<pk>', editar_operadora_telefonica, name='editar_operadora_telefonica'),
    path('operadora/buscar/', buscar_operadora, name='buscar_operadora'),
    
    #*----------------------RUTAS SOCIO----------------------#
    path('socio/registrar/', crear_socio, name='crear_socio'),
    path('socio/lista/', listar_socio, name='listar_socio'),
    path('socio/editar/<pk>/', editar_socio, name='editar_socio'),
    path('socio/buscar/', buscar_socio, name='buscar_socio'),
    #----------------------RUTAS SOCIO----------------------#

    #----------------------RUTAS PROVINCIAS----------------------#
    path('provincias/listar/', listar_provincias, name='listar_provincias'),
    path('provincias/registrar/', agregar_provincia, name='agregar_provincia'), #type:ignore
    path('provincias/editar/<pk>/', editar_provincia, name='editar_provincia'),
    # * ----------------------RUTAS PROVINCIAS----------------------#
    path('provincias/lista/', listar_provincias, name='listar_provincias'),
    path('provincias/registrar/', agregar_provincia, name='agregar_provincia'),
    path('provincias/editar/<pk>', editar_provincia, name='editar_provincia'),
    path('provincias/buscar/', buscar_provincia, name='buscar_provincia'),
    # *----------------------RUTAS PROVINCIAS----------------------#

    path('canton/listar/', listar_canton, name='listar_cantones'),
    path('canton/registrar/', agregar_canton, name='agregar_canton'), #type:ignore
    path('canton/editar/<pk>', editar_canton, name='editar_canton'),
    path('canton/buscar/', buscar_canton, name='buscar_canton'),
    
    path('tipo_fondo/registrar/', crear_tipo_fondo, name='crear_tipo_fondo'), #type:ignore
    # *----------------------RUTAS TIPO FONDO----------------------#
    path('tipo_fondo/registrar/', crear_tipo_fondo, name='crear_tipo_fondo'),
    path('tipo_fondo/listar', listar_tipo_fondo, name='listar_tipo_fondo'),
    path('tipo_fondo/editar/<pk>/', editar_tipo_fondo, name='editar_tipo_fondo'),
    path('tipo_fondo/buscar', buscar_tipo_fondo, name='buscar_tipo_fondo'),
    
    # TODO----------------------RUTAS TIPO FONDO----------------------#
    path('solicitudes_generales/registrar/', agregar_modulo, name='crear_tipo_fondo'),
    path('solicitudes_generales/listar', predeterminado, name='listar_tipo_fondo'),
    path('solicitudes_generales/editar/<pk>/', predeterminado, name='editar_tipo_fondo'),
    path('solicitudes_generales/buscar', predeterminado, name='buscar_tipo_fondo'),
    # TODO----------------------RUTAS TIPO FONDO----------------------#

    path('modulos/registrar/', agregar_modulo, name='agregar_modulo'),
    path('modulos/listar/', listar_modulos, name='listar_modulo'),
    path('modulos/editar/<pk>/', editar_modulo, name='editar_modulo'),
    path('modulos/buscar/', buscar_modulo, name='buscar_modulo'),    
]
