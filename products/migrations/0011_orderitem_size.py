# Generated by Django 4.0.6 on 2022-11-24 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_size_alter_orderitem_order_alter_orderitem_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.ManyToManyField(blank=True, null=True, to='products.size'),
        ),
    ]
