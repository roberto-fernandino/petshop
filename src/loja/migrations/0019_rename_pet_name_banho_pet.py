# Generated by Django 4.2.3 on 2023-08-15 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0018_alter_banhotype_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banho',
            old_name='pet_name',
            new_name='pet',
        ),
    ]
