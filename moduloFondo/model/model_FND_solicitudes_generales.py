from django.db import models


class Model_FND_solicitudes_generales(models.Model):
    
    #modulo_id=models.ForeignKey(,on_delete=models.CASCADE, null=False, blank=False),
    id_solicitud_general = models.BigAutoField(primary_key=True,verbose_name="Id solicitud general"),
    documento = models.TextField(max_length=100,null=False,verbose_name="Documento"),
    plantilla_solicitud_ruta = models.TextField(max_length=None,null=False,verbose_name="Plantilla solicitud ruta"),
    descripcion = models.TextField(max_length=500,null=False,verbose_name="Descripcion"),
    activo = models.TextField(max_length=500,null=False,verbose_name="Activo"),
    fecha_creacion = models.DateTimeField(max_length=500,null=False,auto_now_add=True,verbose_name="Fecha creacion"),
    fecha_modificacion = models.DateTimeField(max_length=500,null=False,auto_now=True,verbose_name="Fecha modificacion"),


    class Meta: 
        app_label = "moduloFondo"
        managed = True
        db_table = 'fnd_solicitudes_generales'
        verbose_name = 'una solicitud general'
        verbose_name_plural = 'solicitudes generales'
        