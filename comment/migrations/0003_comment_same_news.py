# Generated by Django 4.0.4 on 2022-08-23 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_alter_comment_date_alter_comment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='same_news',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
