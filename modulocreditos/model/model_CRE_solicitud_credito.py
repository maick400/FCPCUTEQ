from django.db import models

from moduloCreditos.model.model_CRE_tipo_credito import Model_CRE_tipo_credito
from moduloCreditos.model.model_CRE_tipo_bien import Model_CRE_tipo_bien

class Model_CRE_solicitud_credito (models.Model):
    id_solicitud_credito = models.BigAutoField(primary_key=True)
    #id_fondo_socio = models.ForeignKey(on_delete=models.CASCADE ,null=False)
    id_tipo_credito = models.ForeignKey(Model_CRE_tipo_credito, on_delete=models.CASCADE, null=False, blank=False, default="")
    id_tipo_bien = models.ForeignKey(Model_CRE_tipo_bien, on_delete=models.CASCADE, null=False, blank=False, default="")
    #id_personal_recibido = models.ForeignKey(on_delete=models.CASCADE, null=False)
    #id_personal_validado = models.ForeignKey(on_delete=models.CASCADE, null=False)
    monto = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    numero_cuotas = models.IntegerField(null=False)
    tasa_interes = models.DecimalField(max_digits=3, decimal_places=2, null=False)


    def __str__(self) -> str:
        return (self.id_solicitud_credito)

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_solicitud_credito'
        verbose_name = 'una solicitud de credito'
        verbose_name_plural = 'solicitudes de credito'