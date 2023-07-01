from django.db import models

from moduloFondo.model.Model_FND_provincia import Model_FND_provincia

class Model_FND_canton(models.Model):
    codigo = models.TextField(primary_key=True, max_length=5, verbose_name='Código de cantón', null=False, blank=False)
    cod_provincia = models.ForeignKey(Model_FND_provincia, verbose_name='Código de provincia', db_column='cod_provincia',  null=False, on_delete=models.CASCADE)
    canton = models.TextField(null=False,  verbose_name='Cantón', blank=False)

    class Meta:
        app_label = "moduloFondo"
        constraints = [ 
            models.UniqueConstraint(fields=['codigo'], name='uq_fnd_codigo_canton'),
        ]
        indexes = [
            models.Index(fields=['codigo'])
        ] 
        managed = True
        db_table = 'fnd_canton'
        verbose_name = 'un canton'
        verbose_name_plural = 'cantones'

    


urls_canton = {
            'crear': 'fondo/canton/canton_crear.html',
            'editar': 'fondo/canton/canton_editar.html',
            'listar': 'fondo/canton/canton_listar.html',
            'buscar': 'fondo/canton/canton_buscar.html'
        }