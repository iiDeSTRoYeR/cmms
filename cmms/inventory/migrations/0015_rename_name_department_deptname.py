# Generated by Django 3.2.5 on 2021-08-13 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_merge_20210809_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='Name',
            new_name='deptName',
        ),
    ]
