from flask import Flask, session, render_template, redirect, request
app = Flask(__name__)
app.secret_key = 'rocky'



@app.route("/")
def index(): 
    if session.get('count') is None:
        session['count'] = 1
    else:
        session['count'] = session['count'] + [1]
        session['visit'] = len(session['count'])
        print(session['visit'])

    return render_template("index.html")





app.run(debug=True)