from django.db import models

# Create your models here.


class ContactForm(models.Model):

    name = models.CharField(max_length=60)
    email = models.EmailField()
    msg = models.TextField()
    date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return str(self.name)
