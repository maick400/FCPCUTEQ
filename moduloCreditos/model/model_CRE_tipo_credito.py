from django.db import models

class Model_CRE_tipo_credito (models.Model):
    id_tipo_credito = models.BigAutoField(primary_key=True)
    tipo_credito = models.CharField(max_length=100,null=False, blank=False)
    porc_ahorro_acceso = models.DecimalField(max_digits=3, decimal_places=2, null=False)
    valor_maximo = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    max_credito_anios = models.IntegerField(null=False)
    prioridad_calif_cartera = models.IntegerField(null=False)
    tipo_garan_calif_cartera = models.CharField(max_length=2, null=False)
    permite_garante = models.BooleanField(null=False)
    gerencia_requerida = models.BooleanField(null=False)
    genera_amortizacion = models.BooleanField(null=False)

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_tipo_credito'
        verbose_name = 'un tipo de credito'
        verbose_name_plural = 'tipos de credito'