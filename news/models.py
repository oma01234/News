from __future__ import unicode_literals
from django.db import models

# Create your models here.


class News(models.Model):
    name = models.CharField(max_length=50)
    short_txt = models.TextField()
    body_txt = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    picname = models.TextField()
    picurl = models.ImageField()
    author = models.CharField(max_length=50)
    catname = models.CharField(max_length=50)
    catid = models.IntegerField()
    ncatid = models.IntegerField(default=0)
    show = models.IntegerField()
    tag = models.TextField(default="-")
    act = models.IntegerField(default=0)
    rand = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name) + '|' + str(self.pk)
