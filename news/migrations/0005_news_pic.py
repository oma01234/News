# Generated by Django 4.0.4 on 2022-06-20 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_catid_news_catname_news_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pic',
            field=models.ImageField(default='-', upload_to=''),
            preserve_default=False,
        ),
    ]
