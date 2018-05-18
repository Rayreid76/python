from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "littelceaser"

@app.route('/')
def index():
    if 'a' not in session:
        session['a']= []
    if 'tally' not in session:
        session['tally']= []
    return render_template("index.html", activity=session['a'], tally=session['tally'])

@app.route('/process_farm', methods=['POST','GET'])
def run_farm():
    session['a'] = random.randint(10, 20)
    if 'b' not in session:
        session['b'] = []
    session['b'].append(session['a'])
    session.modified = True
    session['tally'] = sum(session['b'])
    return redirect('/')

@app.route('/process_cave', methods=['POST','GET'])
def run_cave():
    session['a'] = random.randint(5, 10)
    if 'b' not in session:
        session['b'] = []
    session['b'].append(session['a'])
    session['tally'] = sum(session['b'])
    return redirect('/')

@app.route('/process_house', methods=['POST','GET'])
def run_house():
    session['a'] = random.randint(2, 5)
    if 'b' not in session:
        session['b'] = []
    session['b'].append(session['a'])
    session['tally'] = sum(session['b'])
    return redirect('/')

@app.route('/process_casino', methods=['POST','GET'])
def run_casino():
    session['a'] = random.randint(-50, 50)
    if 'b' not in session:
        session['b'] = []
    session['b'].append(session['a'])
    session['tally'] = sum(session['b'])
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')
app.run(debug=True)