from django.urls import path
from core.views import *

app_name = 'core'
urlpatterns = [
    path('', inicio, name='home'),
    path('signin/', iniciar_sesion, name="signin"),
    path('logout/',cerrar_sesion, name="logout"),
   
    path('tablas/',listar_tablas, name="tablas"),
    path('detalle_tabla/<pk>',ver_detalle_tabla, name="detalle_tabla"),
    path('editar_tabla/<pk>',listar_tablas, name="editar_tabla"),
    path('detalle_valor/<pk>',ver_detalle_campo_tabla, name="detalle_valor"),
    path('crear_tabla/',crear_tabla, name="crear_tabla"),
    path('campo_tabla_crear/',crear_campo_tabla, name="campo_tabla_crear"),
    path('crear_valor/',crear_valores_campo, name="crear_valor"),
    path('tabla_estructura/<pk>',tabla_estructura, name="tabla_estructura"),
    path('update_estructura_tabla/<pk>/',update_estructura_tabla, name="update_estructura"),
    path('contable/',modulo_contable, name="mod_contable"),
    path('fondo/',modulo_fondo, name="mod_fondo"),
    path('general/',modulo_general, name="mod_fondo"),
    path('admin-sistema/',modulo_sistema, name="mod_admin"),

    # path('tabla/',get_table, name="tabla"),
]
