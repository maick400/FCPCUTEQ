from django.db import models

from moduloCreditos.model.model_CRE_solicitud_credito import Model_CRE_solicitud_credito

class Model_CRE_credito_otorgado (models.Model):
    id_credito_otorgado = models.BigAutoField(primary_key=True)
    id_solicitud_credito = models.ForeignKey(Model_CRE_solicitud_credito, on_delete=models.CASCADE, null=False)
    #otorgado_por = models.ForeignKey(on_delete=models.CASCADE, null=False)
    monto = models.DecimalField(max_digits=12, decimal_places=12, null=False)
    plazo_meses = models.IntegerField(null=False)
    tasa_interes = models.DecimalField(max_digits=3, decimal_places=2, null=False)
    numero_cuotas = models.IntegerField(null=False)
    fecha_creacion = models.DateField(null=True)
    fecha_modificacion = models.DateField(null = True)

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_credito_otorgado'
        verbose_name = 'una credito otorgado'
        verbose_name_plural = 'creditos otorgados'