# Generated by Django 3.2.5 on 2021-08-06 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20210806_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessory',
            name='Description_ar',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='accessory',
            name='Description_en',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
