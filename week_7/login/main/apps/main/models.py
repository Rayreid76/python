from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class userManage(models.Manager):
    def userValidation(self, fname, lname, email, password, cpassword):
        valid = True
        errors = []
        if len(fname) <= 3:
            valid = False
            errors.append("Error first name is to short")
        elif fname.isalpha() == False:
            valid = False
            errors.append("Error only letters")
        if len(lname) <= 3:
            valid = False
            errors.append("Error last name is to short")
        elif lname.isalpha() == False:
            valid = False
            errors.append("Error only letters")
        if email != "":
            try:
                validate_email(email)
            except ValidationError as e:
                valid = False
                errors.append("Error not valid email")
        if len(password) <= 8:
            valid = False
            errors.append("Error password needs to be 8 characters")
        if cpassword != password:
            valid = False
            errors.append("Error passward does not match")
        else:
            valid = True


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = userManage()

# Create your models here.
