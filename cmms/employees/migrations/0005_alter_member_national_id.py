# Generated by Django 3.2.5 on 2021-07-28 19:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_auto_20210728_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='National_ID',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinValueValidator(1000000000, 'Please Enter 10 Numbers.'), django.core.validators.MaxValueValidator(9999999999, 'Please Enter Less than 10 Numbers.')]),
        ),
    ]
