# Generated by Django 5.1.3 on 2024-11-27 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olxapp', '0007_remove_delivery_orderedimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='myid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olxapp.product'),
        ),
    ]
