# Generated by Django 5.2.4 on 2025-07-15 15:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_shopimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopimage',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
