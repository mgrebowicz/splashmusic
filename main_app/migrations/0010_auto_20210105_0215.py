# Generated by Django 3.1.4 on 2021-01-05 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20210105_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='date',
            field=models.DateTimeField(verbose_name='lesson date'),
        ),
    ]