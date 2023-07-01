from django.urls import path
from moduloFondo.forms import *
from moduloFondo.views import *

app_name = 'fondo'

urlpatterns = [
    path('create/operadora', crear_operadora_telefonica, name='crear_operadora_telefonica'),
    path('list/operadora', listar_operadora_telefonica, name='listar_operadora_telefonica'),
    path('edit/operadora/<pk>', editar_operadora_telefonica, name='editar_operadora_telefonica'),
    path('buscar/operadora/', buscar_operadora, name='buscar_operadora'),


    #----------------------RUTAS SOCIO----------------------#
    path('socio/registrar/', crear_socio, name='crear_socio'),
    path('socio/lista/', listar_socio, name='listar_socio'),
    path('socio/editar/<pk>', editar_socio, name='editar_socio'),
    path('socio/buscar/', buscar_socio, name='buscar_socio'),
    #----------------------RUTAS SOCIO----------------------#

    #----------------------RUTAS PROVINCIAS----------------------#
    path('provincias/lista/', listar_provincias, name='listar_provincias'),
    path('provincias/registrar/', agregar_provincia, name='agregar_provincia'),
    path('provincias/editar/<pk>', editar_provincia, name='editar_provincia'),
    path('provincias/buscar/', buscar_provincia, name='buscar_provincia'),
    #----------------------RUTAS PROVINCIAS----------------------#

    path('canton/listar/', listar_canton, name='listar_cantones'),
    path('canton/registrar/', agregar_canton, name='agregar_canton'),
    path('canton/editar/<pk>', editar_canton, name='editar_canton'),
    path('canton/buscar/', buscar_canton, name='buscar_canton'),
    
     path('create/tipo_fondo', crear_tipo_fondo, name='crear_tipo_fondo'),
    path('list/tipo_fondo', listar_tipo_fondo, name='listar_tipo_fondo'),
    path('edit/tipo_fondo/<pk>', editar_tipo_fondo, name='editar_tipo_fondo'),
    path('buscar/tipo_fondo/', buscar_tipo_fondo, name='buscar_tipo_fondo'),



]
