# Generated by Django 3.1.4 on 2021-01-05 02:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20210105_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]