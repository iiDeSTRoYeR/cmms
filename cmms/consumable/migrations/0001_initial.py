# Generated by Django 3.2.5 on 2021-07-29 22:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(choices=[('محروقات', 'محروقات'), ('ايجار', 'ايجار'), ('مواصلات', 'مواصلات'), ('مستهلكات', 'مستهلكات'), ('مصروفات أخرى', 'مصروفات أخرى')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CostType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(4, 'CostType must be greater than 4 characters')])),
                ('CostClass', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consumable.costclass')),
            ],
        ),
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('DateofBill', models.DateField(null=True)),
                ('Billpdf', models.FileField(null=True, upload_to='bills/')),
                ('CostType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consumable.costtype')),
                ('Member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.member')),
            ],
        ),
    ]
