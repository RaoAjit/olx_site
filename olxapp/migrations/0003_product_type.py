# Generated by Django 5.1.3 on 2024-11-21 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olxapp', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, choices=[('mobile', 'mobile'), ('laptop', 'laptop'), ('upper', 'upper'), ('lower', 'lower')], max_length=20, null=True),
        ),
    ]