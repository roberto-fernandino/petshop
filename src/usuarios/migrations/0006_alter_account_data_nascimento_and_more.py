# Generated by Django 4.2.3 on 2023-08-02 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_remove_account_is_staff_account_cpf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='data_nascimento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
