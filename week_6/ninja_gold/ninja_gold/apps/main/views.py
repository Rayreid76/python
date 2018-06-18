from django.shortcuts import render, redirect
import random

def index(request):
    if 'a' not in request.session:
        request.session['a']= []
    if 'tally' not in request.session:
        request.session['tally']= []
    return render("index.html", activity=request.session['a'], tally=request.session['tally'])


def run_farm(request):
    request.session['a'] = random.randint(10, 20)
    if 'b' not in request.session:
        request.session['b'] = []
    request.session['b'].append(request.session['a'])
    request.session.modified = True
    request.session['tally'] = sum(request.session['b'])
    return redirect('/')


def run_cave(request):
    request.session['a'] = random.randint(5, 10)
    if 'b' not in request.session:
        request.session['b'] = []
    request.session['b'].append(request.session['a'])
    request.session['tally'] = sum(request.session['b'])
    return redirect('/')


def run_house(request):
    request.session['a'] = random.randint(2, 5)
    if 'b' not in request.session:
        request.session['b'] = []
    request.session['b'].append(request.session['a'])
    request.session['tally'] = sum(request.session['b'])
    return redirect('/')


def run_casino(request):
    request.session['a'] = random.randint(-50, 50)
    if 'b' not in request.session:
        request.session['b'] = []
    request.session['b'].append(request.session['a'])
    request.session['tally'] = sum(request.session['b'])
    return redirect('/')



