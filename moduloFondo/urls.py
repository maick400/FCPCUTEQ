from django.urls import path
from moduloFondo.forms import *
from moduloFondo.views import *

app_name = 'fondo'

urlpatterns = [
    path('create/tipo_descuento', crear_tipo_descuento, name='crear_tipo_descuento'),
    path('tipo_descuento', listar_tipo_descuento, name='listar_tipo_descuento'),
    path('edit/tipo_descuento/<pk>', editar_tipo_descuento, name='editar_tipo_descuento'),
    
    path('list/parametros', ver_parametros, name='ver_parametros'),
    path('edit/parametros/<pk>', editar_parametros, name='editar_parametros'),
    path('create/cargo', crear_cargo_empleado, name='crear_cargo_empleado'),
    path('list/cargo', listar_cargo_empleado, name='listar_cargo_empleado'),
    path('edit/cargo/<pk>', editar_cargo_empleado, name='editar_cargo_empleado'),
    path('create/operadora', crear_operadora_telefonica, name='crear_operadora_telefonica'),
    path('list/operadora', listar_operadora_telefonica, name='listar_operadora_telefonica'),
    path('edit/operadora/<pk>', editar_operadora_telefonica, name='editar_operadora_telefonica'),

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

]
