from django.db import models

from moduloCreditos.model.model_CRE_credito_otorgado import Model_CRE_credito_otorgado
from moduloCreditos.model.model_CRE_solicitud_credito import Model_CRE_solicitud_credito


class Model_CRE_credito_garante (models.Model):    
    id_credito_otorgado = models.ForeignKey(Model_CRE_credito_otorgado, on_delete=models.CASCADE, name=False)
    #id_socio = models.ForeignKey(on_delete=models.CASCADE, null=False)
    saldo_cancelado = models.DecimalField(max_digits=12, decimal_places=2, name=False)
    monto_garantia = models.DecimalField(max_digits=12, decimal_places=2, name=False)
    #id_socio = models.ForeignKey(on_delete=models.CASCADE, null=False)
    saldo_cancelado = models.DecimalField(max_digits=12, decimal_places=2, name=False)
    monto_garantia = models.DecimalField(max_digits=12, decimal_places=2, name=False)
    fecha_creacion = models.DateTimeField(null=False)
    fecha_modificacion = models.DateTimeField(null = False)


    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_credito_garante'
        verbose_name = 'un garante para credito'
        verbose_name_plural = 'garantes para credito'