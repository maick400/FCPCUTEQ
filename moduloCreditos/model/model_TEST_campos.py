from django.db import models

from moduloCreditos.model.model_TEST_tabla import Model_TEST_tabla

class Model_TEST_campos (models.Model):
    id_campo = models.BigIntegerField(primary_key=True)
    id_tabla = models.ForeignKey(Model_TEST_tabla, on_delete=models.CASCADE, null=False)
    nombre_campo = models.TextField(null=False, blank=False)    
    tipo_dato = models.TextField(null=False, blank=False)


    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'test_campo'
        verbose_name = 'un campo'
        verbose_name_plural = 'campos'