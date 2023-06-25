from django.db import models

class Model_Fnd_Provincia (models.Model):
    codigo = models.TextField( primary_key=True, max_length=2 )
    provincia = models.TextField(null=False, blank=False, max_length=200)
    
    class Meta:
        app_label = "moduloFondo"
        managed = True
        db_table = 'fnd_provincia'
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
