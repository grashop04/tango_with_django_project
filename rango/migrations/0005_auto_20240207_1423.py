# Generated by Django 2.2.28 on 2024-02-07 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20240206_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.URLField(max_length=128),
        ),
    ]