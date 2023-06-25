from django.db import models

from moduloCreditos.model.model_TEST_campos import Model_TEST_campos

class Model_TEST_valores (models.Model):
    id_valor = models.BigAutoField(primary_key=True)
    id_campo = models.ForeignKey(Model_TEST_campos, on_delete=models.CASCADE, null=False)
    valor = models.TextField(null=False)

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'test_valores'
        verbose_name = 'un valor'
        verbose_name_plural = 'valores'