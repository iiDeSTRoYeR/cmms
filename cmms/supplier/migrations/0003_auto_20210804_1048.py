# Generated by Django 3.2.5 on 2021-08-04 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_auto_20210803_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manufacturer',
            name='Name_ar',
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='Name_en',
        ),
    ]
