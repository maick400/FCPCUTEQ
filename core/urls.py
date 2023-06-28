from django.urls import path
from core.views import *

app_name = 'core'
urlpatterns = [
    path('', inicio, name='home'),
    path('signin/', iniciar_sesion, name="signin"),
    path('logout/',cerrar_sesion, name="logout"),
    path('contable/',modulo_contable, name="mod_contable"),
    path('fondo/',modulo_fondo, name="mod_fondo"),
    path('admin-sistema/',modulo_sistema, name="mod_admin"),



]
