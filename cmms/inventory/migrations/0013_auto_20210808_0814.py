# Generated by Django 3.2.5 on 2021-08-08 05:14

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_accdetail_accmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='bldgno',
            name='campus',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='inventory.campus'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accdetail',
            name='accmodel',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='accessory', chained_model_field='accessory', on_delete=django.db.models.deletion.CASCADE, to='inventory.accmodel', verbose_name="Accessory's Model"),
        ),
        migrations.AlterField(
            model_name='labroom',
            name='blgdno',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='campus', chained_model_field='campus', on_delete=django.db.models.deletion.CASCADE, to='inventory.bldgno'),
        ),
        migrations.AlterField(
            model_name='labroom',
            name='campus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.campus'),
        ),
    ]
