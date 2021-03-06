# Generated by Django 3.2.5 on 2021-08-03 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20210803_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='device_ar',
        ),
        migrations.RemoveField(
            model_name='model',
            name='device_en',
        ),
        migrations.RemoveField(
            model_name='model',
            name='phase_ar',
        ),
        migrations.RemoveField(
            model_name='model',
            name='phase_en',
        ),
        migrations.AddField(
            model_name='phase',
            name='Value_ar',
            field=models.CharField(choices=[('Single Phase', 'Single Phase'), ('Three phase', 'Three phase'), ('DC', 'DC')], max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='phase',
            name='Value_en',
            field=models.CharField(choices=[('Single Phase', 'Single Phase'), ('Three phase', 'Three phase'), ('DC', 'DC')], max_length=20, null=True, unique=True),
        ),
    ]
