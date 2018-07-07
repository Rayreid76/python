from __future__ import unicode_literals

from django.db import models

# Create your models here.
class userManager(models.Manager):
    def validation(self, first_name, last_name, email, password):
        valid = True
        if len(first_name) <= 5:
            valid = False
        if len(last_name) <= 5:
            valid = False
        if len(email) <= 5:
            valid = False
        return True
        

class registure(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = userManager()