from django.db import models
from moduloCreditos.model.model_CRE_solicitud_credito import Model_CRE_solicitud_credito

class Model_CRE_solicitud_credito_documentos (models.Model):
    id_solicitud_credito = models.ForeignKey(Model_CRE_solicitud_credito, on_delete=models.CASCADE, null=False)
    nombre_documento = models.CharField(max_length=200, null=False, blank=False)
    ruta_documento = models.CharField(max_length=99999, null=False, blank=False)
    estado = models.CharField(max_length=1, null=False, blank=False)
    fecha_creacion = models.DateField(null=True)
    fecha_modificacion = models.DateField(null = True)
   
    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_solicitud_credito_documentos'
        verbose_name = 'un documento para solicitud de credito'
        verbose_name_plural = 'documentos para solicitud de credito'