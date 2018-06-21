from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        "user": users.objects.all()
    }
    return render(request,"main/index.html", context)

def create(request):
    return render(request, "main/create.html")

def add(request):
    fullname = request.POST["fullname"]
    email = request.POST["email"]
    valid = users.objects.validates(fullname, email)
    if valid:
        users.objects.create(fullname=fullname,email=email)
        return redirect("/")
    else:
        return HttpResponse("Name error")

def show(request, user_id):
    context = {
        "user": users.objects.get(id=user_id)
    }
    return render(request, "main/show.html", context)

def edit(request, user_id):
    context = {
        "user": users.objects.get(id=user_id)
    }
    return render(request, "main/edit.html", context)

def change(request, user_id):
    b = users.objects.get(id=user_id)
    b.fullname = request.POST["name"]
    b.email = request.POST["email"]    
    b.save()
    return redirect("/")

def delete(request, user_id):
    b = users.objects.get(id=user_id)
    b.delete()
    return redirect("/")
    