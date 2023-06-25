from django.db import models

from moduloCreditos.model.model_CRE_tipo_credito import Model_CRE_tipo_credito

class Model_CRE_tipo_credito_montos (models.Model):
    id_tipo_credito = models.ForeignKey(Model_CRE_tipo_credito, on_delete=models.CASCADE, blank=False, null=False)
    monto_inicial = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    monto_final = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    plazo_maximo_meses = models.IntegerField(null=False)
    fecha_creacion = models.DateTimeField(null=False)
    fecha_modificacion = models.DateTimeField(null = False)

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_tipo_credito_montos'
        verbose_name = 'una monto del tipo de credito'
        verbose_name_plural = 'montos de un tipo de credito'
