from django.db import models

from moduloFondo.model.Model_FND_provincia import Model_FND_provincia

class Model_FND_canton(models.Model):
    codigo = models.TextField(primary_key=True, max_length=5, null=False, blank=False)
    cod_provincia = models.ForeignKey(Model_FND_provincia, null=False, on_delete=models.CASCADE)
    canton = models.TextField(null=False, blank=False)

    class Meta:
        app_label = "moduloFondo"
        managed = True
        db_table = 'fnd_canton'
        verbose_name = 'un canton'
        verbose_name_plural = 'cantones'