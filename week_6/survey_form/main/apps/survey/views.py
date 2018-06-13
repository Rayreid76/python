from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request,"survey/index.html")

def results(request):
    request.session["name"] = request.POST["name"]
    request.session["location"] = request.POST["location"]
    request.session["lang"] = request.POST["lang"]
    request.session["comments"] = request.POST["comments"]
    return render(request, "survey/results.html")
    

# Create your views here.
