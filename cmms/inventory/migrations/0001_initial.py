# Generated by Django 3.2.5 on 2021-07-19 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
        ('spareparts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, unique=True)),
                ('College', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.college')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('PPM_Cycle', models.IntegerField(blank=True, null=True)),
                ('BriefFunctionDes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DeviceClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceMainType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Operational', 'Operational'), ('Malfunctioning', 'Malfunctioning')], max_length=50, unique=True)),
                ('condition', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, unique=True)),
                ('Phone_Number', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('frequency', models.DecimalField(decimal_places=3, max_digits=3)),
                ('voltage', models.IntegerField()),
                ('amperage', models.DecimalField(decimal_places=3, max_digits=3)),
                ('phase', models.IntegerField()),
                ('device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.device')),
                ('manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.manufacturer')),
                ('spareParts', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='spareparts.sparepart')),
            ],
        ),
        migrations.CreateModel(
            name='LabRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, unique=True)),
                ('BlgdNo', models.IntegerField()),
                ('FloorNo', models.IntegerField()),
                ('GPSCoor', models.CharField(max_length=100)),
                ('Department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.department')),
                ('Operator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.operator')),
                ('campus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.campus')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceAsset',
            fields=[
                ('Asset_No', models.IntegerField(blank=True, primary_key=True, serialize=False, unique=True)),
                ('Serial_Number', models.CharField(max_length=50)),
                ('DevicePic', models.FileField(upload_to='')),
                ('DownTime', models.DateTimeField(blank=True, null=True)),
                ('DeviceStatus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.devicestatus')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.device')),
                ('lab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.labroom')),
                ('warranty', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.warranty')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='Device_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.deviceclass'),
        ),
        migrations.AddField(
            model_name='device',
            name='accessories',
            field=models.ManyToManyField(to='inventory.Accessory'),
        ),
        migrations.AddField(
            model_name='campus',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.device'),
        ),
        migrations.AddField(
            model_name='accessory',
            name='AccModel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.accmodel'),
        ),
        migrations.AddField(
            model_name='accessory',
            name='devices',
            field=models.ManyToManyField(to='inventory.Device'),
        ),
        migrations.CreateModel(
            name='AccDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=500)),
                ('SerialNo', models.IntegerField()),
                ('accessory', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='inventory.accessory')),
            ],
        ),
    ]