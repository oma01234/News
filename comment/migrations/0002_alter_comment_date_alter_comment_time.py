# Generated by Django 4.0.4 on 2022-08-23 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.CharField(max_length=15),
        ),
    ]
