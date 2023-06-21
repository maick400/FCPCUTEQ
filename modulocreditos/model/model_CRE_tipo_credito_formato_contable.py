from django.db import models

from moduloCreditos.model.model_CRE_tipo_credito import Model_CRE_tipo_credito

class Model_CRE_tipo_credito_formato_contable (models.Model):
    id_tipo_credito = models.ForeignKey(Model_CRE_tipo_credito, on_delete=models.CASCADE, blank=False, null=False)
    #id_cuenta_diario_contable_plantilla = models.ForeignKey(, on_delete=models.CASCADE, blank=False, null=False)
    #asiento_contable = models.IntegerField(null=False, default="")
    
    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_tipo_credito_formato_contable'
        verbose_name = 'una formato contable para tipo de credito'
        verbose_name_plural = 'formatos contables para tipo de credito'