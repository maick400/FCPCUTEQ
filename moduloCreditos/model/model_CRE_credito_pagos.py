from django.db import models

from moduloCreditos.model.model_CRE_credito_otorgado import Model_CRE_credito_otorgado

class Model_CRE_credito_pagos (models.Model):
    id_credito_otorgado = models.ForeignKey(Model_CRE_credito_otorgado, on_delete=models.CASCADE, null=False)
    #id_personal_receptor = models.ForeignKey(on_delete=models.CASCADE, null=False)
    numero_cuota = models.IntegerField(null=False)
    fecha_cancelacion = models.DateTimeField(null=False)
    pago_interes = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    fecha_creacion = models.DateField(null=True)
    fecha_modificacion = models.DateField(null = True)
    

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'credito_pagos'
        verbose_name = 'un pago para credito'
        verbose_name_plural = 'pagos para credito'