from django.db import models

from moduloCreditos.model.model_CRE_tipo_bien import Model_CRE_tipo_bien

class Model_CRE_tipo_bien_documento (models.Model):
    id_tipo_bien = models.ForeignKey(Model_CRE_tipo_bien, on_delete=models.CASCADE, null=False)
    nombre_documento = models.CharField(max_length=200, null=False, blank=False)
    fecha_creacion = models.DateField(null=True)
    es_requerido = models.DateField(null=True)
    fecha_modificacion = models.DateField(null = True)

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_tipo_bien_documento'
        verbose_name = 'una tipo de de documento para un bien'
        verbose_name_plural = 'documentos para un bien'