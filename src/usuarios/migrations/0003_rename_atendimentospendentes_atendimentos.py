# Generated by Django 4.2.3 on 2023-07-31 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_atendimentospendentes_assunto_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AtendimentosPendentes',
            new_name='Atendimentos',
        ),
    ]
