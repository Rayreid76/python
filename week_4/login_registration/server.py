from flask import Flask, redirect, render_template,flash, request, session
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'askjdfhaisdgf'
mysql = MySQLConnector(app,'login_registration1')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reg')
def regist():
    return render_template('registration.html')

@app.route('/user')
def user():
    user = mysql.query_db("select * from users")
    return render_template('user.html', all_user=user)

@app.route('/registration', methods=["post"])
def create():
    if len(request.form['uname']) < 1:
        flash("User Name is blank!!!")
        return redirect('/reg')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Not valid email")
        return redirect('/reg')
    elif len(request.form['pword']) < 1:
        flash("Password is blank")
        return redirect('/reg')
    elif len(request.form['lname']) < 1:
        flash("Last name is blank")
        return redirect('/reg')
    elif len(request.form['fname']) < 1:
        flash("First name is blank")
        return redirect('/reg')
    else:
        flash("Success! You are registured")
    print("start")    
    uname = request.form["uname"]
    email = request.form["email"]
    pword = request.form["pword"]
    fname = request.form["fname"]
    lname = request.form["lname"]
    print("values")
    query = "INSERT INTO users (`first_name`, `last_name`, `password`, `created_at`, `updated_at`, `user_name`, `email`) VALUES (:fname, :lname, :pword, now(), now(), :uname, :email);"
    print("insert")
    data = {
             'user_name':uname,
             'email':email,
             'password':pword,
             'first_name':fname,
             'last_name':lname
            }
    print("data")
    user = mysql.query_db(query, data)
    print("mysql")
    return redirect('/user')       

app.run(debug=True)