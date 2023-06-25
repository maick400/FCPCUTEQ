from django.db import models


class Model_CORE_tabla (models.Model):
    id_tabla = models.BigAutoField(primary_key=True)
    nombre_tabla = models.TextField(null=False, blank=False)
    numero_tabla = models.BigIntegerField(null=False)

    class Meta:
        app_label = "core"
        managed = True
        db_table = 'core_tabla'
        verbose_name = 'una tabla'
        verbose_name_plural = 'tablas'