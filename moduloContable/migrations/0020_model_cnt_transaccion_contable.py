# Generated by Django 4.2.1 on 2023-06-17 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moduloContable', '0019_model_asiento_contable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model_CNT_Transaccion_Contable',
            fields=[
                ('idTransaccion_Contable', models.BigAutoField(primary_key=True, serialize=False)),
                ('detalle', models.CharField(max_length=100)),
                ('ultimaLinea', models.IntegerField()),
                ('estado', models.BooleanField()),
                ('IdTipoTransaccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloContable.model_cnt_tipo_transaccion_contable')),
            ],
            options={
                'verbose_name': 'un Socio',
                'verbose_name_plural': 'Socios',
                'db_table': 'CNT_Transaccion_Contable',
                'managed': True,
            },
        ),
    ]