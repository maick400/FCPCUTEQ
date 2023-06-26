from django.db import models


class Model_CORE_solicitudes_generales (models.Model):    
    id_solicitud_general = models.BigAutoField(primary_key=True)
    documento_solicitud = models.TextField(null=False, blank=False)
    plantilla_solicitud = models.TextField()
    modulo = models.CharField(max_length=10)
    descripcion = models.TextField()
    activo = models.BooleanField(null=False)
    fecha_creacion = models.DateTimeField(null=False)
    fecha_modificacion = models.DateTimeField(null=False)


    class Meta:
        app_label = "core"
        managed = True
        db_table = 'core_solicitudes_generales'
        verbose_name = 'una solicitud general'
        verbose_name_plural = 'solicitudes generales'