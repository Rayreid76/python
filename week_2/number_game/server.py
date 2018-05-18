from flask import Flask, session, redirect, request, render_template, flash
import random
app = Flask(__name__)
app.secret_key = 'hotdog'



@app.route("/")
def index():
    session['n'] = random.randint(0, 100)
    print(session['n'])
    return render_template("index.html")

@app.route("/game", methods=["POST"])
def play_game():
       
    new_input = request.form['number']    
    if session['n'] < int(new_input):
        session['an'] = ["Too high"]
        new_input = request.form['number']
    elif session['n'] > int(new_input):
        session['an'] = ["Too low"]
        new_input = request.form['number']
    else:
        session['an'] = ("The number is", session['n'])
    return render_template("index.html", result = session['an'])

@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")



app.run(debug=True)