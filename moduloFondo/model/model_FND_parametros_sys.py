from django.db import models
from moduloFondo.model.model_FND_socio import Model_FND_socio as SOCIO
from moduloFondo.model.model_FND_tipo_identificación import * 
from core.tools.get_field import Core_Tabla




class Model_FND_Parametros_sys(models.Model):
    

    
    provincia = models.CharField(max_length=300,null=False, blank=False)

    
    
    


    class Meta: 
        app_label = "moduloFondo"
        managed = True
        db_table = 'fnd_parametros_sistema'
        verbose_name = 'un Parametro'
        verbose_name_plural = 'Parametros'