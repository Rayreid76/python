from django.shortcuts import render, HttpResponse, redirect
from models import * 


from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your views here.
def index(request):
    return render(request,"main/index.html")

def register(request):
    fname = request.POST["first_name"]
    lname = request.POST["last_name"]
    email = request.POST["email"]
    password = request.POST["password"]
    cpassword = request.POST["confirm_password"]
    valid = True
    if len(fname) <= 3:
        valid = False
        print ("Error first name is to short")
    elif fname.isalpha() == False:
        valid = False
        print("Error only letters")
    if len(lname) <= 3:
        valid = False
        print ("Error last name is to short")
    elif lname.isalpha() == False:
        valid = False
        print("Error only letters")
    if email != "":
        try:
            validate_email(email)
        except ValidationError as e:
            valid = False
            print "Error not valid email"
        else:
            print "hooray! email is valid"
    if len(password) <= 8:
        valid = False
        print("Error password needs to be 8 characters")
    if cpassword != password:
        valid = False
        print("Error passward does not match")
    else:
        Users.objects.create(first_name=fname, last_name=lname, email=email, password=password)
    return redirect("/")

def login(request):
    return redirect("/")

    #r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
