# Generated by Django 4.2.3 on 2023-08-02 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_alter_account_data_nascimento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
