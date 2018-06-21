from __future__ import unicode_literals

from django.db import models

# Create your models here.
class userManager(models.Manager):
    def validates(self, fullname, email):
        valid = True
        if fullname == "":
            valid = False
        if email == "":
            valid = False
        return valid
        
class users(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = userManager()