from django.shortcuts import render, HttpResponse, redirect
from .models import * 
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request,"main/index.html")

def register(request):
    fname = request.POST["first_name"]
    lname = request.POST["last_name"]
    email = request.POST["email"]
    password = request.POST["password"]
    cpassword = request.POST["confirm_password"]
    errors = Users.objects.userValidation(fname, lname, email, password, cpassword)
    
    if len(errors) == 0:
        hashed = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
        Users.objects.create(first_name=fname, last_name=lname, email=email, password=hashed)
        
        return redirect("/")
    else: #add message to html
        
        for message in errors:
            messages.error(request, message)
        return redirect("/")

def login(request):
    email = request.POST["email"]
    password = request.POST["password"] 
    result = Users.objects.loginVal(email, password)
    if result[0]:
        request.session["id"] = result[1]
        return redirect("/dashboard")
    else: #add message to html
        for message in result[1]:
            messages.error(request, message)
        return redirect("/")
def dashboard(request):
    return HttpResponse("got to dashboard")
