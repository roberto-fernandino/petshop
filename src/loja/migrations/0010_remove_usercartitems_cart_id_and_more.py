# Generated by Django 4.2.3 on 2023-08-12 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0009_usercart_usercartitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercartitems',
            name='cart_id',
        ),
        migrations.RemoveField(
            model_name='usercartitems',
            name='produto',
        ),
        migrations.DeleteModel(
            name='UserCart',
        ),
        migrations.DeleteModel(
            name='UserCartItems',
        ),
    ]