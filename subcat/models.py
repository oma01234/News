from __future__ import unicode_literals
#  helps database to adapt to languages
from django.db import models

# Create your models here.


class SubCat(models.Model):

    name = models.CharField(max_length=50)
    catname = models.CharField(max_length=50)
    catid = models.IntegerField()
    # when creating new data, the default= is to set any value for that variable if it doesnt have one

    def __str__(self):
        return self.name
