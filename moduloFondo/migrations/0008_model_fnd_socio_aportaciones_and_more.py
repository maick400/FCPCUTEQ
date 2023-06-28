# Generated by Django 4.2.1 on 2023-06-17 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moduloFondo', '0007_remove_model_fnd_socio_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model_FND_socio_aportaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_aportacion', models.DateField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloFondo.model_fnd_personal')),
                ('id_socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloFondo.model_fnd_socio')),
                ('id_tipo_descuento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloFondo.model_fnd_tipo_descuento')),
            ],
            options={
                'verbose_name': 'una aportación',
                'verbose_name_plural': 'Aportaciones',
                'db_table': 'FND_socio_aportaciones',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_FND_contacto_socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10, unique=True)),
                ('estado', models.BooleanField()),
                ('predeterminado', models.BooleanField(unique=True)),
                ('id_operadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloFondo.model_fnd_operadora_telf')),
                ('id_socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloFondo.model_fnd_socio')),
            ],
            options={
                'verbose_name': 'un Contacto Socio',
                'verbose_name_plural': 'Contactos Socios',
                'db_table': 'FND_contacto_socio',
                'managed': True,
            },
        ),
    ]
