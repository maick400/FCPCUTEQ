from django.db import models

class Model_FND_operadora_telf(models.Model):
    operadora_id = models.BigAutoField(primary_key=True)
    operadora = models.CharField(max_length=20,blank=False,null=False,unique=True)


    class Meta:
        app_label = "moduloFondo"
        managed = True
        db_table = 'fnd_operadora_telf'
        verbose_name = 'una operadora'
        verbose_name_plural = 'las operadoras'