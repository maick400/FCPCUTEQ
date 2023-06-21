from django.db import models
from moduloCreditos.model.model_CRE_credito_otorgado import Model_CRE_credito_otorgado

class Model_CRE_credito_amortizacion (models.Model):
    id_credito_otorgado = models.ForeignKey(Model_CRE_credito_otorgado, default="", on_delete=models.CASCADE, null=False)
    numero_cuota = models.IntegerField(null=False)
    fecha_pago = models.DateTimeField(null=False)
    pago_capital = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    pago_interes = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    seguro_desgravamen = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    cuota_total = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    saldo_actual = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    dias_vencidos = models.IntegerField(null=False)

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_credito_amortizacion'
        verbose_name = 'una amortizacion de credito'
        verbose_name_plural = 'amortizaciones de credito'