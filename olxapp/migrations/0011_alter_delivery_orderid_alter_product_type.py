# Generated by Django 5.1.3 on 2024-12-06 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olxapp', '0010_alter_cart_myid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='orderid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olxapp.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('electronics', 'electronics'), ('vehicles', 'vehicles'), ('furniture', 'furniture'), ('houses', 'house')], max_length=20),
        ),
    ]
