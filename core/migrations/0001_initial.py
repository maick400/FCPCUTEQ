# Generated by Django 4.2.1 on 2023-06-25 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model_CORE_campos',
            fields=[
                ('id_campo', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre_campo', models.TextField()),
                ('tipo_dato', models.TextField()),
            ],
            options={
                'verbose_name': 'un campo de tabla',
                'verbose_name_plural': 'campos de tabla',
                'db_table': 'core_campo_tabla',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CORE_solicitudes_generales',
            fields=[
                ('id_solicitud_general', models.BigAutoField(primary_key=True, serialize=False)),
                ('documento_solicitud', models.TextField()),
                ('plantilla_solicitud', models.TextField()),
                ('modulo', models.CharField(max_length=10)),
                ('descripcion', models.TextField()),
                ('activo', models.BooleanField()),
                ('fecha_creacion', models.DateTimeField()),
                ('fecha_modificacion', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'una solicitud general',
                'verbose_name_plural': 'solicitudes generales',
                'db_table': 'core_solicitudes_generales',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CORE_tabla',
            fields=[
                ('id_tabla', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_tabla', models.TextField()),
                ('numero_tabla', models.BigIntegerField()),
            ],
            options={
                'verbose_name': 'una tabla',
                'verbose_name_plural': 'tablas',
                'db_table': 'core_tabla',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CORE_valores',
            fields=[
                ('id_valor', models.BigAutoField(primary_key=True, serialize=False)),
                ('valor', models.TextField()),
                ('activo', models.BooleanField()),
                ('id_campo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.model_core_campos')),
            ],
            options={
                'verbose_name': 'un valor de un campo',
                'verbose_name_plural': 'valores de un campo',
                'db_table': 'core_valor_campo',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='model_core_campos',
            name='id_tabla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.model_core_tabla'),
        ),
    ]
