# Generated by Django 4.0.6 on 2022-11-29 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_order_has_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='has_size',
        ),
    ]
