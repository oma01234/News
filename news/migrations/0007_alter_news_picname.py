# Generated by Django 4.0.4 on 2022-06-21 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_rename_pic_news_picname_news_picurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='picname',
            field=models.TextField(),
        ),
    ]
