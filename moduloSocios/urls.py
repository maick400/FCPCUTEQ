from django.urls import path
from moduloSocios.forms import *
from moduloSocios.views import *


app_name = 'socio'

urlpatterns = [
    path('create/', crear_socio, name='crear_socio')
]