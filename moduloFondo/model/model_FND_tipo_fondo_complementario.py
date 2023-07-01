from django.db import models

class Model_FND_tipo_fondo_complementario(models.Model):
    codigo = models.TextField(primary_key=True, max_length=5, null=False, blank=False)
    tipo = models.TextField(null=False, blank=False,verbose_name="tipo")
    descripcion = models.TextField(blank=False, null=False,verbose_name="descripcion")

    class Meta:
        app_label = "moduloFondo"
        constraints=[
            models.UniqueConstraint(fields=["codigo"],name="uq_fnd_codigo_id"),
            models.UniqueConstraint(fields=["tipo"],name="uq_fnd_tipo"),
            models.UniqueConstraint(fields=["descripcion"],name="uq_fnd_descripcion")
        ]
        indexes=[models.Index(fields=["codigo"])]
        managed = True
        db_table = 'fnd_tipo_fondo_complementario'
        verbose_name = 'un tipo de fondo complementario'
        verbose_name_plural = 'Tipos de fondo complementarios'



urls_tipo_fondo = {
            'crear': 'fondo/tipo_fondo_complementario/tipo_fondo_crear.html',
            'editar': 'fondo/tipo_fondo_complementario/tipo_fondo_editar.html',
            'listar': 'fondo/tipo_fondo_complementario/tipo_fondo_lista.html',
            'buscar': 'fondo/tipo_fondo_complementario/tipo_fondo_busqueda.html'
}