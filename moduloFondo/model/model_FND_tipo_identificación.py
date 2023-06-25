from django.db import models

class Model_Fnd_Tipo_Identificacion (models.Model):
    codigo = models.TextField(max_length=1, null=False, blank=False)
    descripción_tipo_identificacion = models.TextField(max_length=300, null= False, blank=False)
    class Meta:
        app_label = "moduloFondo"
        managed = True
        db_table = 'fnd_tipo_identificacion'
        verbose_name = 'Tipo identificación'
        verbose_name_plural = 'Tipos de identificaciones'