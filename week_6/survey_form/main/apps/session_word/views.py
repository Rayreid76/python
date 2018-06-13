from django.shortcuts import render, redirect, HttpResponse

def index(request):
    if request.method == "GET":
        return render(request, "session_word/index.html")

# Create your views here.
def create(request):
    if request.method == "GET":
        return render(request, "session_word/index.html")
    elif request.method == "POST":
        request.session["name"] = request.POST["name"]
        request.session["color"] = request.POST["color"]
        return render(request, "session_word/index.html")