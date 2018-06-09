from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'random_word/index.html')


def word(request, method="POST"):
    context = {
        "random_word": get_random_string(length=14),
        "attemt": 12121
    }
    return render(request, 'random_word/index.html', context)


# Create your views here.
