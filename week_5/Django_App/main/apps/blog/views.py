from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "hello blogs"
    return HttpResponse(response)

def new1(request):
    response = "hello new"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number):
    print "Blog: "+ number
    return HttpResponse("Blog " + number)

def edit(request, number):
    print "Blog edit: " + number
    return HttpResponse("Blog edit " + number)

def destroy(request, number):
    print number
    return redirect('/')

# Create your views here.
