from django.db import models

class Model_FND_provincia(models.Model):
    codigo = models.TextField(primary_key=True, max_length=5, null=False, blank=False)
    provincia = models.TextField(null=False, blank=False, max_length=100)

    class Meta:
        app_label = "moduloFondo"
        managed = True
        db_table = 'fnd_provincia'
        verbose_name = 'una provincia'
        verbose_name_plural = 'provincias'