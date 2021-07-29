# Generated by Django 3.2.5 on 2021-07-28 19:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_alter_member_national_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(choices=[('Engineer', 'Engineer'), ('Technician', 'Technician'), ('Labor', 'Labor'), ('Administrator', 'Administrator')], max_length=100, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='member',
            old_name='Nationality',
            new_name='nationality',
        ),
        migrations.RemoveField(
            model_name='member',
            name='ExpPassPort',
        ),
        migrations.RemoveField(
            model_name='member',
            name='Title',
        ),
        migrations.AddField(
            model_name='member',
            name='ExpPassport',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='ExpID',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='ExpSCE',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='Experience',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='Experience_PDF',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='member',
            name='ID_PDF',
            field=models.FileField(upload_to='employees/id/<django.db.models.fields.BigIntegerField>'),
        ),
        migrations.AlterField(
            model_name='member',
            name='Lapses',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='MobileNo',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(500000000, 'Please Enter 10 Numbers.'), django.core.validators.MaxValueValidator(599999999, 'Please Enter Less than 10 Numbers.')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='Passport_PDF',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='member',
            name='Qualification',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='SCE_PDF',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='member',
            name='Salary',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='member',
            name='Warnings',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='jobtitle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.jobtitle'),
        ),
    ]