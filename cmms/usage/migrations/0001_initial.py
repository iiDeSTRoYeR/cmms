# Generated by Django 3.2.5 on 2021-07-29 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UsageRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inTimeStamp', models.DateTimeField(auto_now_add=True)),
                ('Duration', models.DateTimeField(blank=True, null=True)),
                ('outTimeStamp', models.DateTimeField(blank=True, null=True)),
                ('deviceasset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.deviceasset')),
                ('deviceuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]