from django.db import models

# Create your models here.
class Contact(models.Model):
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.username