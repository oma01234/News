# Generated by Django 4.0.4 on 2022-06-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='pic',
            new_name='picname',
        ),
        migrations.AddField(
            model_name='news',
            name='picurl',
            field=models.ImageField(default='-', upload_to=''),
            preserve_default=False,
        ),
    ]
