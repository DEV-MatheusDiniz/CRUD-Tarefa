# Generated by Django 4.1 on 2022-08-31 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0004_alter_tarefa_data_alteracao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='data_cadastro',
            field=models.DateTimeField(verbose_name='data/hora'),
        ),
    ]
