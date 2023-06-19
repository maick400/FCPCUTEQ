from django.db import models

from moduloCreditos.model.model_CRE_credito_bien import Model_CRE_credito_bien

class Model_CRE_credito_bien_solicitud (models.Model):
    id_credito_bien = models.ForeignKey(Model_CRE_credito_bien, on_delete=models.CASCADE, blank=False, null=False)
    nombre_documento = models.CharField(max_length=200, null=False, blank=False)
    ruta_documento = models.CharField(max_length=1000, null=False, blank=False)

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_tipo_bien_solicitud'
        verbose_name = 'una solicitud de bien'
        verbose_name_plural = 'solicitudes de bien'