from __future__ import unicode_literals

from django.db import models

class Contact(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    emailaddr = models.CharField(max_length=200)
    birthday = models.DateField(max_length=200)
    addr = models.CharField(max_length=200)
    phone_number = models.IntegerField(max_length=11)

    

