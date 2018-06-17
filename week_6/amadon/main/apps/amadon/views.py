from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = {
        "items":[
            {"name":"Skateboard", "price":"$185.00", "id":"18500"},
            {"name":"Skies", "price":"$550.00", "id":"55000"},
            {"name":"Mountian Bike", "price":"$350.00", "id":"35000"},
            {"name":"Jetski", "price":"$1400.00", "id":"140000"},
        ]
    }
    return render(request, "amadon/index.html", context)

def sales(request):
    if request.method == "GET":
        return redirect("/")
    if request.method == "POST":
        if request.session['quantity'] == 0:
            return redirect("/")
        else:
            request.session['product_id'] = request.POST['product_id']
            request.session['quantity'] = request.POST['quantity']
            return render(request, "amadon/checkout.html")