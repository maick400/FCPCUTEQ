from django.db import models

from moduloCreditos.model.model_TEST_campos import Model_TEST_campos

class Model_TEST_validaciones (models.Model):
    id_validaciones = models.BigAutoField(primary_key=True)
    id_campo = models.ForeignKey(Model_TEST_campos, on_delete=models.CASCADE, null=False)
    tipo_validacion = models.TextField(null=False)
    valor_validacion = models.TextField(null = False)    


    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'test_validaciones'
        verbose_name = 'una validación'
        verbose_name_plural = 'validaciones'