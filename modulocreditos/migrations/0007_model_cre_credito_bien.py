# Generated by Django 4.2.1 on 2023-06-19 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloCreditos', '0006_model_cre_bien_documentos'),
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
    ]
