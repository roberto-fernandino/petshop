# Generated by Django 4.2.3 on 2023-08-05 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=100)),
                ('setor', models.CharField(max_length=50)),
                ('preco', models.FloatField()),
                ('descricao', models.TextField(null=True)),
                ('imagem', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
