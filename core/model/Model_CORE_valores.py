from django.db import models

from core.model.Model_CORE_campos import Model_CORE_campos

class Model_CORE_valores (models.Model):
    id_valor = models.BigAutoField(primary_key = True)
    id_campo = models.ForeignKey(Model_CORE_campos, on_delete=models.CASCADE, null=False)
    valor = models.TextField(null = False)
    activo = models.BooleanField(null = False)

    class Meta:
        app_label = "core"
        managed = True
        db_table = 'core_valor_campo'
        verbose_name = 'un valor de un campo'
        verbose_name_plural = 'valores de un campo'