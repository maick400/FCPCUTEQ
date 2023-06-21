from django.urls import path
from moduloFondo.forms import *
from moduloFondo.views import *

app_name = 'fondo'

urlpatterns = [
    path( 'create/tipo_descuento', crear_tipo_descuento, name='crear_tipo_descuento'),
    path( 'list/tipo_descuento', listar_tipo_descuento, name='listar_tipo_descuento'),
    path( 'edit/tipo_descuento/<pk>', editar_tipo_descuento, name='editar_tipo_descuento'),
    path('create/socio', crear_socio, name='crear_socio'),
    path('list/socio', listar_socio, name='lista_socio'),
    path('edit/socio/<pk>', editar_socio, name='editar_socio'),
    path('list/parametros', ver_parametros, name='ver_parametros'),
    path('edit/parametros/<pk>', editar_parametros, name='editar_parametros'),

]