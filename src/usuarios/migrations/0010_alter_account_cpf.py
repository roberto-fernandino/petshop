# Generated by Django 4.2.3 on 2023-08-05 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_account_data_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='cpf',
            field=models.CharField(max_length=14, null=True, unique=True),
        ),
    ]
