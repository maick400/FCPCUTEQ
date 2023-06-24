# Generated by Django 4.2.1 on 2023-06-21 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model_CRE_credito_bien',
            fields=[
                ('id_credito_bien', models.BigAutoField(primary_key=True, serialize=False)),
                ('bien', models.CharField(max_length=200)),
                ('avaluo', models.DecimalField(decimal_places=2, max_digits=12)),
                ('atributos', models.CharField(blank=True, max_length=99999, null=True)),
            ],
            options={
                'verbose_name': 'un crédito por bien',
                'verbose_name_plural': 'créditos por bien',
                'db_table': 'cre_tipo_credito_bien',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CRE_credito_otorgado',
            fields=[
                ('id_credito_otorgado', models.BigAutoField(primary_key=True, serialize=False)),
                ('monto', models.DecimalField(decimal_places=12, max_digits=12)),
                ('plazo_meses', models.IntegerField()),
                ('tasa_interes', models.DecimalField(decimal_places=2, max_digits=3)),
                ('numero_cuotas', models.IntegerField()),
            ],
            options={
                'verbose_name': 'una credito otorgado',
                'verbose_name_plural': 'creditos otorgados',
                'db_table': 'cre_credito_otorgado',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CRE_solicitud_bien',
            fields=[
                ('id_solicitud_bien', models.BigAutoField(primary_key=True, serialize=False)),
                ('avaluo', models.DecimalField(decimal_places=2, max_digits=12)),
                ('bien', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=1)),
                ('atributo', models.CharField(max_length=99999)),
            ],
            options={
                'verbose_name': 'una solicitud por bien',
                'verbose_name_plural': 'solicitudes por bien',
                'db_table': 'cre_solicitud_bien',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CRE_solicitud_credito',
            fields=[
                ('id_solicitud_credito', models.BigAutoField(primary_key=True, serialize=False)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=12)),
                ('numero_cuotas', models.IntegerField()),
                ('tasa_interes', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
            options={
                'verbose_name': 'una solicitud de credito',
                'verbose_name_plural': 'solicitudes de credito',
                'db_table': 'cre_solicitud_credito',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CRE_tipo_bien',
            fields=[
                ('id_tipo_bien', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_bien', models.CharField(max_length=100)),
                ('avaluo', models.DecimalField(decimal_places=2, max_digits=12)),
                ('observacion', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'un tipo de bien',
                'verbose_name_plural': 'tipo de bienes',
                'db_table': 'cre_tipo_bien',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CRE_tipo_credito',
            fields=[
                ('id_tipo_credito', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipo_credito', models.CharField(max_length=100)),
                ('porc_ahorro_acceso', models.DecimalField(decimal_places=2, max_digits=3)),
                ('valor_maximo', models.DecimalField(decimal_places=2, max_digits=12)),
                ('max_credito_anios', models.IntegerField()),
                ('prioridad_calif_cartera', models.IntegerField()),
                ('tipo_garan_calif_cartera', models.CharField(max_length=2)),
                ('permite_garante', models.BooleanField()),
                ('gerencia_requerida', models.BooleanField()),
                ('genera_amortizacion', models.BooleanField()),
            ],
            options={
                'verbose_name': 'un tipo de credito',
                'verbose_name_plural': 'tipos de credito',
                'db_table': 'cre_tipo_credito',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CRE_tipo_credito_montos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_inicial', models.DecimalField(decimal_places=2, max_digits=12)),
                ('monto_final', models.DecimalField(decimal_places=2, max_digits=12)),
                ('plazo_maximo_meses', models.IntegerField()),
                ('id_tipo_credito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_tipo_credito')),
            ],
            options={
                'verbose_name': 'una monto del tipo de credito',
                'verbose_name_plural': 'montos de un tipo de credito',
                'db_table': 'cre_tipo_credito_montos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CRE_tipo_credito_docs_requeridos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_documento', models.CharField(max_length=200)),
                ('es_requerido', models.BooleanField()),
                ('id_tipo_credito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_tipo_credito')),
            ],
            options={
                'verbose_name': 'un documento requerido para credito',
                'verbose_name_plural': 'documentos requeridos para credito',
                'db_table': 'cre_tipo_credito_docs_requeridos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CRE_tipo_credito_cuentas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, null=True)),
                ('id_tipo_credito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_tipo_credito')),
            ],
            options={
                'verbose_name': 'una cuenta del tipo de credito',
                'verbose_name_plural': 'cuentas de un tipo de credito',
                'db_table': 'cre_tipo_credito_cuentas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CRE_tipo_bien_tipo_credito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField()),
                ('id_tipo_bien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_tipo_bien')),
                ('id_tipo_credito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_tipo_credito')),
            ],
            options={
                'verbose_name': 'una tipo de bien para credito',
                'verbose_name_plural': 'tipos de bien para creditos',
                'db_table': 'cre_tipo_bien_tipo_credito',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CRE_tipo_bien_documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_documento', models.CharField(max_length=200)),
                ('id_tipo_bien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_tipo_bien')),
            ],
            options={
                'verbose_name': 'una tipo de de documento para un bien',
                'verbose_name_plural': 'documentos para un bien',
                'db_table': 'cre_tipo_bien_documento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CRE_tipo_bien_atributo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atributo', models.CharField(max_length=100)),
                ('tipo_dato', models.CharField(max_length=100)),
                ('obligatorio', models.BooleanField()),
                ('id_tipo_bien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_tipo_bien')),
            ],
            options={
                'verbose_name': 'un atributo de un tipo de bien',
                'verbose_name_plural': 'atributos de un tipo de bien',
                'db_table': 'cre_tipo_bien_atributos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CRE_solicitud_documentos_bien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_documento', models.CharField(max_length=200)),
                ('ruta_documento', models.CharField(max_length=999999)),
                ('id_solicitud_bien', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_solicitud_bien')),
            ],
            options={
                'verbose_name': 'un documento para solicitud por bien',
                'verbose_name_plural': 'documentos para solicitud por bien',
                'db_table': 'cre_solicitud_documentos_bien',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CRE_solicitud_credito_documentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_documento', models.CharField(max_length=200)),
                ('ruta_documento', models.CharField(max_length=99999)),
                ('estado', models.CharField(max_length=1)),
                ('id_solicitud_credito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_solicitud_credito')),
            ],
            options={
                'verbose_name': 'un documento para solicitud de credito',
                'verbose_name_plural': 'documentos para solicitud de credito',
                'db_table': 'cre_solicitud_credito_documentos',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='model_cre_solicitud_credito',
            name='id_tipo_bien',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_tipo_bien'),
        ),
        migrations.AddField(
            model_name='model_cre_solicitud_credito',
            name='id_tipo_credito',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_tipo_credito'),
        ),
        migrations.AddField(
            model_name='model_cre_solicitud_bien',
            name='id_solicitud_credito',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_solicitud_credito'),
        ),
        migrations.CreateModel(
            name='Model_CRE_credito_pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cancelacion', models.DateTimeField()),
                ('numero_cuota', models.IntegerField()),
                ('pago_interes', models.DecimalField(decimal_places=2, max_digits=12)),
                ('id_credito_otorgado', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_credito_otorgado')),
            ],
            options={
                'verbose_name': 'un pago para credito',
                'verbose_name_plural': 'pagos para credito',
                'db_table': 'credito_pagos',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='model_cre_credito_otorgado',
            name='id_solicitud_credito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_solicitud_credito'),
        ),
        migrations.CreateModel(
            name='Model_CRE_credito_garante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo_credito_actual', models.DecimalField(decimal_places=2, max_digits=12)),
                ('id_credito_otorgado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_credito_otorgado')),
                ('id_solicitud_credito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_solicitud_credito')),
            ],
            options={
                'verbose_name': 'un garante para credito',
                'verbose_name_plural': 'garantes para credito',
                'db_table': 'cre_credito_garante',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CRE_credito_documentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_documento', models.CharField(max_length=200)),
                ('ruta_documento', models.CharField(max_length=99999)),
                ('id_credito_otorgado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_credito_otorgado')),
            ],
            options={
                'verbose_name': 'una documento para credito',
                'verbose_name_plural': 'documentos para credito',
                'db_table': 'cre_credito_documentos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CRE_credito_bien_solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_documento', models.CharField(max_length=200)),
                ('ruta_documento', models.CharField(max_length=1000)),
                ('id_credito_bien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_credito_bien')),
            ],
            options={
                'verbose_name': 'una solicitud de bien',
                'verbose_name_plural': 'solicitudes de bien',
                'db_table': 'cre_tipo_bien_solicitud',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='model_cre_credito_bien',
            name='id_credito_otorgado',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_credito_otorgado'),
        ),
        migrations.CreateModel(
            name='Model_CRE_credito_amortizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_cuota', models.IntegerField()),
                ('fecha_pago', models.DateTimeField()),
                ('pago_capital', models.DecimalField(decimal_places=2, max_digits=12)),
                ('pago_interes', models.DecimalField(decimal_places=2, max_digits=12)),
                ('seguro_desgravamen', models.DecimalField(decimal_places=2, max_digits=12)),
                ('cuota_total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('saldo_actual', models.DecimalField(decimal_places=2, max_digits=12)),
                ('dias_vencidos', models.IntegerField()),
                ('id_credito_otorgado', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_credito_otorgado')),
            ],
            options={
                'verbose_name': 'una amortizacion de credito',
                'verbose_name_plural': 'amortizaciones de credito',
                'db_table': 'cre_credito_amortizacion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model_CRE_bien_documentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_documento', models.CharField(max_length=200)),
                ('ruta_documento', models.CharField(max_length=1000)),
                ('id_bien_solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloCreditos.model_cre_tipo_bien')),
            ],
            options={
                'verbose_name': 'un documento requerido',
                'verbose_name_plural': 'documentos requeridos',
                'db_table': 'cre_bien_documentos',
                'managed': True,
            },
        ),
    ]
