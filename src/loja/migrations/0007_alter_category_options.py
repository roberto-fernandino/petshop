# Generated by Django 4.2.3 on 2023-08-09 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0006_category_produto_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]