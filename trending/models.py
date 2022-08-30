from __future__ import unicode_literals
#  helps database to adapt to languages
from django.db import models

# Create your models here.


class Trending(models.Model):

    txt = models.CharField(max_length=200)

    def __str__(self):
        return str(self.txt)

