# Generated by Django 4.0.4 on 2022-08-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_comment_same_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
