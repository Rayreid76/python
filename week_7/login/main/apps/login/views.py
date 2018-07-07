from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "login/index.html")

def registure(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    valid = registure.objects.validation()
    if valid:
        registure.objects.create(first_name=first_name,last_name=last_name,email=email,password=password)
        return redirect("login/user.html")
    return HttpResponse("Registure")

def login(request):
    return HttpResponse("login")