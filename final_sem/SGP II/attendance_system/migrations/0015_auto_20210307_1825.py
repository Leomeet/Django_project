# Generated by Django 3.0.8 on 2021-03-07 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_system', '0014_remove_attendance_is_in_or_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
    ]