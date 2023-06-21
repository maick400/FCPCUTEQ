from django.db import models

from moduloCreditos.model.model_CRE_tipo_credito import Model_CRE_tipo_credito

class Model_CRE_tipo_credito_monto (models.Model):
    id_tipo_credito = models.ForeignKey(Model_CRE_tipo_credito, on_delete=models.CASCADE, blank=False, null=False)
    monto_inicial = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    monto_final = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    plazo_meses = models.IntegerField(null=False)
    
    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_tipo_credito_monto'
        verbose_name = 'un monto para tipo de credito'
        verbose_name_plural = 'montos para tipo de credito'