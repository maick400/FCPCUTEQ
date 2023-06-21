# Generated by Django 4.2.1 on 2023-06-17 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moduloContable', '0013_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model_CNT_Cuenta_Contable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cuenta', models.CharField(max_length=100)),
                ('Naturaleza', models.CharField(max_length=100)),
                ('movimiento_mayor', models.CharField(max_length=100)),
                ('nivel', models.SmallIntegerField()),
                ('cuc_reg', models.BooleanField()),
                ('Estado', models.BooleanField()),
                ('cuenta_ContableCodigo', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloContable.model_cnt_cuenta_contable')),
            ],
            options={
                'verbose_name': 'un Socio',
                'verbose_name_plural': 'Socios',
                'db_table': 'CNT_Cuenta_Contable',
                'managed': True,
            },
        ),
    ]
