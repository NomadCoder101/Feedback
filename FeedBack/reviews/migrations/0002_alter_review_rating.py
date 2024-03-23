# Generated by Django 5.0.2 on 2024-03-17 14:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message=None), django.core.validators.MaxValueValidator(5, message=None)]),
        ),
    ]
