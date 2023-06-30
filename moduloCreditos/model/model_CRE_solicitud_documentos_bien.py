from django.db import models

from moduloCreditos.model.model_CRE_solicitud_bien import Model_CRE_solicitud_bien

class Model_CRE_solicitud_documentos_bien (models.Model):
    id_solicitud_bien = models.ForeignKey(Model_CRE_solicitud_bien, default = "", on_delete=models.CASCADE, blank=False, null=False)
    nombre_documento = models.CharField(max_length=200, null=False, blank=False)
    ruta_documento = models.CharField(max_length=999999, null=False, blank=False)
    fecha_creacion = models.DateField(null=True)
    fecha_modificacion = models.DateField(null = True)

    def __str__(self) -> str:
        return (self.id_solicitud_bien)

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_solicitud_documentos_bien'
        verbose_name = 'un documento para solicitud por bien'
        verbose_name_plural = 'documentos para solicitud por bien'