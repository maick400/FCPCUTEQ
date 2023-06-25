from django.db import models

from moduloCreditos.model.model_CRE_tipo_credito import Model_CRE_tipo_credito

class Model_CRE_tipo_credito_cuentas (models.Model):
    id_tipo_credito = models.ForeignKey(Model_CRE_tipo_credito, on_delete=models.CASCADE, blank=False, null=False)
    #id_cuenta_cuentable = models.ForeignKey(, on_delete=models.CASCADE, blank=False, null=False)
    descripcion = models.CharField(max_length=200, null=True)
    fecha_creacion = models.DateTimeField(null=False)
    fecha_modificacion = models.DateTimeField(null = False)
    

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_tipo_credito_cuentas'
        verbose_name = 'una cuenta del tipo de credito'
        verbose_name_plural = 'cuentas de un tipo de credito'