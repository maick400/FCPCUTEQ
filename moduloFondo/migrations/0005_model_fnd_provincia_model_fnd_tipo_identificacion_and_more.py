# Generated by Django 4.2.1 on 2023-06-28 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moduloFondo', '0004_merge_20230625_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model_Fnd_Provincia',
            fields=[
                ('codigo', models.TextField(max_length=2, primary_key=True, serialize=False)),
                ('provincia', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
                'db_table': 'fnd_provincia',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_Fnd_Tipo_Identificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.TextField(max_length=1)),
                ('descripción_tipo_identificacion', models.TextField(max_length=300)),
            ],
            options={
                'verbose_name': 'Tipo identificación',
                'verbose_name_plural': 'Tipos de identificaciones',
                'db_table': 'fnd_tipo_identificacion',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='model_fnd_parametros_sys',
            name='direccion',
            field=models.TextField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='model_fnd_parametros_sys',
            name='email',
            field=models.TextField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='model_fnd_parametros_sys',
            name='fecha_resolucion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='model_fnd_parametros_sys',
            name='identificacion',
            field=models.TextField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='model_fnd_parametros_sys',
            name='n_resolucion',
            field=models.TextField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='model_fnd_socio',
            name='estado',
            field=models.CharField(choices=[('A', 'ACTIVO'), ('I', 'INACTIVO')], max_length=3),
        ),
        migrations.AlterField(
            model_name='model_fnd_socio',
            name='estado_civil',
            field=models.CharField(choices=[('SOL', 'Soltero/a'), ('CAS', 'Casado/a'), ('DIV', 'Divorciado/a'), ('VIU', 'Viudo/a'), ('ULB', 'Unión libre')], max_length=3),
        ),
        migrations.AlterField(
            model_name='model_fnd_socio',
            name='genero',
            field=models.CharField(choices=[('MAS', 'Masculino'), ('FEM', 'FEmenino'), ('ND', 'No definido')], max_length=3),
        ),
        migrations.AlterField(
            model_name='model_fnd_socio',
            name='tipo_prestacion',
            field=models.CharField(choices=[('QUI', 'Quirografario'), ('PRE', 'Prendario')], max_length=3),
        ),
        migrations.CreateModel(
            name='Model_Fnd_Canton',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.TextField(max_length=2)),
                ('canton', models.TextField(max_length=200)),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloFondo.model_fnd_provincia')),
            ],
            options={
                'verbose_name': 'Un cantón',
                'verbose_name_plural': 'Cantones',
                'db_table': 'fnd_canton',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='model_fnd_parametros_sys',
            name='canton',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloFondo.model_fnd_canton'),
        ),
        migrations.AddField(
            model_name='model_fnd_parametros_sys',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloFondo.model_fnd_provincia'),
        ),
        migrations.AddField(
            model_name='model_fnd_parametros_sys',
            name='tipo_de_idemtificacion_fcpc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloFondo.model_fnd_tipo_identificacion'),
        ),
    ]