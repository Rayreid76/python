from django.shortcuts import render, HttpResponse, redirect
import bcrypt
from .models import *
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, "belt/index.html")

def login(request):
    return render(request, "belt/login.html")

def register(request):
    return render(request, "belt/register.html")

def record(request):
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    email = request.POST["email"]
    password = request.POST["password"]
    cpassword = request.POST["cpassword"]
    errors = Users.objects.userValidation(fname, lname, email, password, cpassword)    
    if len(errors) == 0:
        hashed = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
        Users.objects.create(first_name=fname, last_name=lname, email=email, password=hashed, user_level="normal")        
        return redirect("/login")
    else: #add message to html        
        for message in errors:
            messages.error(request, message)
        return redirect("/register")

def signin(request):
    email = request.POST["email"]
    password = request.POST["password"] 
    result = Users.objects.loginVal(email, password)
    if result[0]:
        request.session["id"] = result[1]
        return redirect("/dashboard")
    else: #add message to html
        for message in result[1]:
            messages.error(request, message)
        return redirect("/login")
def dashboard(request):
    player = Users.objects.get(id=request.session['id'])
    context = {
        "user": Users.objects.get(id=request.session["id"]),
        "everyone": Users.objects.all()
    }
    if player.user_level == "admin":
        return render(request, "belt/admindashboard.html", context)
    else:
        return render(request, "belt/dashboard.html", context)

def logout(request):
    request.session.clear()
    return redirect("/login")

def wall(request):
    context = {
        "user": Users.objects.get(id=request.session['id']),
        "post": Posts.objects.filter(user_id=request.session['id']),
        "wall": Posts.objects.all(),
        "comment": Comments.objects.all()
    }
    return render(request, "belt/wall.html", context)

def create_post(request):    
    Posts.objects.create(post=request.POST["posting"], user_id=request.session['id'])
    return redirect("/wall")

def delete_post(request, id):
    Posts.objects.get(id=id).delete()
    return redirect("/wall")

# the wall comments
def make_comment(request, id):
    Comments.objects.create(comment=request.POST["commenting"],user_id=request.session['id'], post_id=id)
    return redirect("/wall")

# edit user
def profile(request):
    context = {
        "user": Users.objects.get(id=request.session['id']),
    }
    return render(request, "belt/update.html", context)

def edit_user_name(request):
    user = request.session['id']
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    pulled = Users.objects.get(id = user)
    if fname != "":
        pulled.first_name=fname
        pulled.save()
    if lname != "":
        pulled.last_name=lname
        pulled.save()
    if email != "":
        pulled.email=email
        pulled.save()
    print pulled
    return redirect("/dashboard")

def edit_user_password(request):
    password = request.POST['password']
    cpassword = request.POST['cpassword']
    user = request.session['id']
    pulled = Users.objects.get(id=user)
    if password == cpassword:
        hashed = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
        pulled.password = hashed
        pulled.save()
    else:
        print "Error"
    return redirect("/dashboard")
# delete user
def delete_user(request, id):
    Users.objects.get(id=id).delete()
    return redirect("/dashboard")

def adminupdate(request, id):
    context = {
        "user": Users.objects.get(id = id)
    }
    return render(request, "belt/adminupdate.html", context)
def edit_admin_name(request, id):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    pulled = Users.objects.get(id = id)
    if fname != "":
        pulled.first_name=fname
        pulled.save()
    if lname != "":
        pulled.last_name=lname
        pulled.save()
    if email != "":
        pulled.email=email
        pulled.save()
    print pulled
    return redirect("/dashboard")
def edit_admin_password(request, id):
    password = request.POST['password']
    cpassword = request.POST['cpassword']
    pulled = Users.objects.get(id=id)
    if password == cpassword:
        hashed = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
        pulled.password = hashed
        pulled.save()
    else:
        print "Error"
    return redirect("/dashboard")

def add_user(request):
    return render(request, "belt/add_user.html")