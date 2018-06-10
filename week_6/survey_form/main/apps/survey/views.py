from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request,"survey/index.html")

def results(request):
    

# Create your views here.
