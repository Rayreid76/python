from django.shortcuts import render, redirect, HttpResponse

def index(request):
    if request.method == "GET":
        print "get"
        return render(request, "session_word/index.html")

# Create your views here.
