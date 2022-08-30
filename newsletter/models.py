from __future__ import unicode_literals
from django.db import models

# Create your models here.


class NewsLetter(models.Model):
    txt = models.CharField(max_length=50)
    status = models.IntegerField()
    
    def __str__(self):
        return str(self.txt)
