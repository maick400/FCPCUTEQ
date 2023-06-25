from django.db import models
from moduloCreditos.model.model_CRE_credito_otorgado import Model_CRE_credito_otorgado

class Model_CRE_credito_documentos (models.Model):
    id_credito_otorgado = models.ForeignKey(Model_CRE_credito_otorgado, on_delete=models.CASCADE, blank=False)
    fuente_documento = models.CharField(max_length=1, null=False, blank=False)
    nombre_documento = models.CharField(max_length=200, blank=False, null=False)
    ruta_documento = models.CharField(max_length=99999, blank=False, null=False)
    fecha_creacion = models.DateTimeField(null=False)
    fecha_modificacion = models.DateTimeField(null = False)

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_credito_documentos'
        verbose_name = 'una documento para credito'
        verbose_name_plural = 'documentos para credito'