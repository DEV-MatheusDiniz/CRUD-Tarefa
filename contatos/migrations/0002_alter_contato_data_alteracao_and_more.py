# Generated by Django 4.1 on 2022-08-31 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_alteracao',
            field=models.DateTimeField(blank=True, null=True, verbose_name='data/hora'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='data_cadastro',
            field=models.DateTimeField(verbose_name='data/hora'),
        ),
    ]