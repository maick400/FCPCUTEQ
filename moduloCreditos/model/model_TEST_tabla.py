from django.db import models


class Model_TEST_tabla (models.Model):
    id_tabla = models.BigIntegerField(primary_key=True)
    nombre_tabla = models.TextField(null=False, blank=False)    

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'test_tabla'
        verbose_name = 'una tabla'
        verbose_name_plural = 'tablas'