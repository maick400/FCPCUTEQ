from django.urls import path
from moduloCreditos.views import *

app_name = 'creditos'

urlpatterns = [
    path( 'crear_tipo_Credito/', crear_tipo_credito, name='crear_tipo_credito')
]
