from django.db import models
from moduloCreditos.model.model_CRE_tipo_bien import Model_CRE_tipo_bien

class Model_CRE_bien_documentos (models.Model):
    id_bien_solicitud = models.ForeignKey(Model_CRE_tipo_bien, on_delete=models.CASCADE, null=False, blank=False)
    nombre_documento = models.CharField(max_length=200, null=False, blank=False)
    ruta_documento = models.CharField(max_length=1000, null=False, blank=False)
    fecha_creacion = models.DateField(null=True, blank=True)
    fecha_modificacion = models.DateField(null = True, blank=True)

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_bien_documentos'
        verbose_name = 'un documento requerido'
        verbose_name_plural = 'documentos requeridos'