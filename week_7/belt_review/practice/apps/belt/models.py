from __future__ import unicode_literals

from django.db import models
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import bcrypt

# Create your models here.
class userManage(models.Manager):
    def userValidation(self, fname, lname, email, password, cpassword):
        errors = []
        if len(fname) <= 3:
            
            errors.append("Error first name is to short")
        elif fname.isalpha() == False:
            
            errors.append("Error only letters")
        if len(lname) <= 3:
            
            errors.append("Error last name is to short")
        elif lname.isalpha() == False:
            
            errors.append("Error only letters")
        if email != "":
            
            try:
                validate_email(email)
            except ValidationError as e:
                
                errors.append("Error not valid email")
        if len(password) < 8:
            
            errors.append("Error password needs to be 8 characters")
        if cpassword != password:
            
            errors.append("Error passward does not match")
        else:
            
            return errors

    def loginVal(self, email, password):
        errors = []
        if email == "":
            errors.append("Email cannot be blank!")
        if password == "":
            errors.append("Password cannot be blank!")
        else:
            users = self.filter(email=email)
            if len(users) > 0:
                user = users[0]
                coded = b'password'
                if bcrypt.checkpw(coded.encode(), user.password.encode()):
                    return (True, user.id) 
                else:
                    errors.append("Incorrect password")
            else:
                errors.append("No email found")
        return (False, errors)

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    user_level = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManage()

class Posts(models.Model):
    post = models.TextField()
    user = models.ForeignKey(Users, related_name="publish")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    comment = models.CharField(max_length=255)
    user = models.ForeignKey(Users, related_name="response")
    post = models.ForeignKey(Posts, related_name="response")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

