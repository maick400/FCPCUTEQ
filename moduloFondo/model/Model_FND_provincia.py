from django.db import models

class Model_FND_provincia(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5, verbose_name='codigo de provincia',null=False, blank=False)
    provincia = models.CharField(null=False, blank=False, verbose_name='provincia', max_length=100)

    def __str__(self):
        return self.provincia

    class Meta:
        app_label = "moduloFondo"
        constraints = [
            models.UniqueConstraint(fields=['codigo'], name='uq_fnd_codigo_provincia'),
            models.UniqueConstraint(fields=['provincia'], name='uq_fnd_provincia')
        ]
        indexes = [
            models.Index(fields=['codigo'])
        ] 
        managed = True
        db_table = 'fnd_provincia'
        verbose_name = 'una provincia'
        verbose_name_plural = 'provincias'

urls_provincia = {
            'crear': 'fondo/provincia/provincia_crear.html',
            'editar': 'fondo/provincia/provincia_editar.html',
            'listar': 'fondo/provincia/provincia_listar.html',
            'buscar': 'fondo/provincia/provincia_buscar.html'
        }