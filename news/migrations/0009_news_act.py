# Generated by Django 4.0.4 on 2022-07-05 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_news_ncatid'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='act',
            field=models.IntegerField(default=0),
        ),
    ]
