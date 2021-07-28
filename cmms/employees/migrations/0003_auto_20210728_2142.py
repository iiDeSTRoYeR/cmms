# Generated by Django 3.2.5 on 2021-07-28 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20210726_0801'),
        ('employees', '0002_auto_20210728_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationslog',
            name='Lab',
        ),
        migrations.RemoveField(
            model_name='locationslog',
            name='Member',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='Member',
        ),
        migrations.AddField(
            model_name='locationslog',
            name='lab',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inventory.labroom'),
        ),
        migrations.AddField(
            model_name='locationslog',
            name='member',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='employees.member'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='member',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.member'),
        ),
        migrations.AlterField(
            model_name='locationslog',
            name='OutTime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='VehicleType',
            field=models.CharField(choices=[('Sedan', 'Sedan'), ('Truck', 'Truck')], default='Sedan', max_length=50),
        ),
    ]
