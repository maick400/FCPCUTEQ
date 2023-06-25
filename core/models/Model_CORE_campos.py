from django.db import models

from core.models.Model_CORE_tabla import Model_CORE_tabla

class Model_CORE_campos (models.Model):
    id_campo = models.BigIntegerField(primary_key=True)
    id_tabla = models.ForeignKey(Model_CORE_tabla, on_delete=models.CASCADE, null=False)
    nombre_campo = models.TextField(null=False, blank=False)    
    tipo_dato = models.TextField(null=False, blank=False)


    class Meta:
        app_label = "core"
        managed = True
        db_table = 'core_campo_tabla'
        verbose_name = 'un campo de tabla'
        verbose_name_plural = 'campos de tabla'