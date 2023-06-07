from django.urls import path
from core.views import *

app_name = 'core'
urlpatterns = [
    path('', inicio, name='home'),
    path('signin/', iniciar_sesion, name="signin"),
    path('logout/',cerrar_sesion, name="logout"),

]
