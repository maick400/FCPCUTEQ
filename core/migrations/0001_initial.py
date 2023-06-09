
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
                ('id_campo', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_campo', models.TextField()),
            ],
            options={
                'verbose_name': 'un campo de tabla',
                'verbose_name_plural': 'campos de tabla',
                'db_table': 'core_campo_tabla',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CORE_tabla',
            fields=[
                ('id_tabla', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_tabla', models.TextField()),
                ('ente_provee_tabla', models.TextField(null=True)),
                ('numero_tabla', models.BigIntegerField(null=True)),
                ('descripcion', models.TextField(null=True)),
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
                ('linea', models.BigIntegerField()),
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
