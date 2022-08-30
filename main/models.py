from __future__ import unicode_literals
#  helps database to adapt to languages
from django.db import models

# Create your models here.


class Main(models.Model):

    name = models.CharField(max_length=30)
    about = models.TextField()
    abouttxt = models.TextField(default=" ")
    fb = models.CharField(default="-", max_length=30)
    tw = models.CharField(default="-", max_length=30)
    yt = models.CharField(default="-", max_length=30)
    tell = models.CharField(default="-", max_length=30)
    link = models.CharField(default="-", max_length=30)
    picurl = models.ImageField(default="-")
    picname = models.CharField(default="-", max_length=30)

    # when creating new data, the default= is to set any value for that variable if it doesnt have one

    def __str__(self):
        return str(self.name) + '|' + str(self.pk)
