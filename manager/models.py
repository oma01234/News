from __future__ import unicode_literals
#  helps database to adapt to languages
from django.db import models

# Create your models here.


class Manager(models.Model):

    name = models.CharField(max_length=30)
    utxt = models.TextField()
    email = models.EmailField(default="pass@gmail.com")
    ip = models.TextField(default="")
    country = models.TextField(default="")

    def __str__(self):
        return str(self.name) + '|' + str(self.pk)
