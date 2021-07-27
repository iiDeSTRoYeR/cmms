# Generated by Django 3.2.5 on 2021-07-19 13:21

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
                ('Title', models.CharField(choices=[], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CostType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('CostClass', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consumable.costclass')),
            ],
        ),
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('CostType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consumable.costtype')),
                ('Member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.member')),
            ],
        ),
    ]