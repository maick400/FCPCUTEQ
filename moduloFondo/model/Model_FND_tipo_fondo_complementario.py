from django.db import models

class Model_FND_tipo_fondo_complementario(models.Model):
    codigo = models.TextField(primary_key=True, max_length=5, null=False, blank=False)
    tipo = models.TextField(null=False, blank=False)
    descripcion = models.TextField(blank=False, null=False)

    class Meta:
        app_label = "moduloFondo"
        managed = True
        db_table = 'fnd_tipo_fondo_complementario'
        verbose_name = 'un tipo de fondo complementario'
        verbose_name_plural = 'Tipos de fondo complementarios'