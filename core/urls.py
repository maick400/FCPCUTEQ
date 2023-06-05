from django.urls import path
from core.views import *

app_name = 'core'
urlpatterns = [
    path('signin/',signin, name="signin"),
    path('logout/',signin, name="logout"),

]
