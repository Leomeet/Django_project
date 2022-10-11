# Generated by Django 3.0.8 on 2021-03-07 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_system', '0012_auto_20210306_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='in_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='is_in_or_out',
            field=models.BooleanField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='out_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
