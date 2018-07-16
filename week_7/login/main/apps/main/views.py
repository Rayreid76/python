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
    errors = Users.objects.userValidation(fname, lname, email, password,cpassword)
    if len(errors) == 0:
        Users.objects.create(first_name=fname, last_name=lname, email=email, password=password)
        return redirect("/")
    else: #add message to html
        for message in errors:
            message.error(request, message)
        return redirect("/")

def login(request):
    return redirect("/")
