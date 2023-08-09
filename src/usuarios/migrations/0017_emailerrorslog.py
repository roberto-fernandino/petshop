# Generated by Django 4.2.3 on 2023-08-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0016_account_groups_account_user_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailErrorsLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150)),
                ('log', models.CharField(default='None', max_length=255, null=True)),
                ('error_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]