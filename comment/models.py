from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    cm = models.TextField()
    news_id = models.IntegerField()
    status = models.IntegerField(default=0)
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=15)
    same_news = models.CharField(max_length=50, default="-")

    def __str__(self):
        return str(self.name) + ' commented on ' + str(self.same_news)
