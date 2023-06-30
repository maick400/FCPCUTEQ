from django.db import models

from moduloCreditos.model.model_CRE_tipo_credito import Model_CRE_tipo_credito

class Model_CRE_tipo_credito_docs_requeridos (models.Model):
    id_tipo_credito = models.ForeignKey(Model_CRE_tipo_credito, on_delete=models.CASCADE, blank=False, null=False)
    nombre_documento = models.CharField(max_length=200, null=False, blank=False)
    es_requerido = models.BooleanField(null=False, blank=False)
    fecha_creacion = models.DateField(null=True)
    fecha_modificacion = models.DateField(null = True)

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_tipo_credito_docs_requeridos'
        verbose_name = 'un documento requerido para credito'
        verbose_name_plural = 'documentos requeridos para credito'