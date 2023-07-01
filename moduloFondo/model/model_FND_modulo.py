from django.db import models

class Model_FND_modulo(models.Model):
    id_modulo = models.BigAutoField(primary_key=True, verbose_name='ID Módulo')
    nombre_modulo = models.TextField(max_length=100,blank=False,null=False, verbose_name='Nombre del módulo')
    app_label = models.TextField(max_length=100,blank=False,null=False, verbose_name='Nombre de la app')
    url_modulo = models.TextField(blank=False,null=False,verbose_name='URL del módulo')
    foto_modulo_ruta = models.ImageField(max_length=1000, blank=False,null=False,verbose_name='Foto del módulo', upload_to='moduloFondo/modulo/')
    descripcion = models.TextField(blank=False,null=False, verbose_name='Descripción')
    activo = models.BooleanField(null=False, verbose_name='Activo')
    fecha_creacion = models.DateTimeField(blank=False,null=False, auto_now_add=True, verbose_name='Fecha de creación')
    fecha_modificacion = models.DateTimeField(blank=False,null=False, auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        app_label = "moduloFondo"
        constraints = [
            models.UniqueConstraint(fields=['nombre_modulo'], name='uq_fnd_modulo_id_modulo')
        ]
        indexes = [
            models.Index(fields=['id_modulo'])
        ]
        managed = True
        db_table = 'fnd_modulo'
        verbose_name = 'un modulo'
        verbose_name_plural = 'modulos'

urls_modulo = {
    'crear': 'fondo/modulo/modulo_crear.html',
    'editar': 'fondo/modulo/modulo_editar.html',
    'listar': 'fondo/modulo/modulo_listar.html',
    'buscar': 'fondo/modulo/modulo_buscar.html'
}