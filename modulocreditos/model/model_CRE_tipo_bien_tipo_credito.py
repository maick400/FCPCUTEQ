from django.db import models

from moduloCreditos.model.model_CRE_tipo_credito import Model_CRE_tipo_credito
from moduloCreditos.model.model_CRE_tipo_bien import Model_CRE_tipo_bien

class Model_CRE_tipo_bien_tipo_credito (models.Model):
    id_tipo_credito = models.ForeignKey(Model_CRE_tipo_credito, on_delete=models.CASCADE, blank=False, null=False)
    id_tipo_bien =  models.ForeignKey(Model_CRE_tipo_bien, on_delete=models.CASCADE, blank=False, null=False)
    estado = models.BooleanField(null = False)

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_tipo_bien_tipo_credito'
        verbose_name = 'una tipo de bien para credito'
        verbose_name_plural = 'tipos de bien para creditos'