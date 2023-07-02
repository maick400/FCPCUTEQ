from django.db import models

#modulo_id=models.ForeignKey(,on_delete=models.CASCADE, null=False, blank=False),

class Model_FND_solicitudes_generales(models.Model):
    
    fecha_creacion=models.DateTimeField(null=False,auto_now_add=True,verbose_name="Fecha_creacion")
    fecha_modificacion=models.DateTimeField(null=False,auto_now=True,verbose_name="Fecha_modificacion")

    id_solicitud_general=models.BigAutoField(primary_key=True,verbose_name="Id_solicitud_general")
    documento=models.TextField(max_length=None,null=False,verbose_name="Documento")
    plantilla_solicitud_ruta=models.FileField(max_length=None,null=False,verbose_name="Plantilla_solicitud_ruta",upload_to="moduloFondo/solicitudesGenerales/")
    descripcion=models.TextField(max_length=500,null=False,verbose_name="Descripcion")
    activo=models.BooleanField(null=False,verbose_name="Activo")



    class Meta: 
        app_label = "moduloFondo"
        managed = True
        db_table = 'fnd_solicitudes_generales'
        verbose_name = 'una solicitud general'
        verbose_name_plural = 'Solicitud general'


