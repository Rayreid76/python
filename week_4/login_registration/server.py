from flask import Flask, redirect, render_template,flash, request, session
from mysqlconnection import MySQLConnector
import re, md5
password = 'password'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'askjdfhaisdgf'
mysql = MySQLConnector(app,'login_registration1')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['post'])
def login():
    password = md5.new(request.form['pword']).hexdigest()
    uname = request.form['uname']
    user_query = "SELECT * FROM users where users.user_name = :uname AND users.password = :pword"
    query_data = { 'uname': uname, 'pword': password}
    user = mysql.query_db(user_query, query_data)
    return redirect('/user')

@app.route('/reg')
def regist():
    return render_template('registration.html')

@app.route('/user')
def user():
    user = mysql.query_db("select * from users")
    return render_template('user.html', all_user=user)

@app.route('/registration', methods=['post'])
def create():
    if len(request.form['uname']) < 1:
        flash("User Name is blank!!!")
        return redirect('/reg')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Not valid email")
        return redirect('/reg')
    elif len(request.form['pword']) <= 8:
        flash("Password is blank")
        return redirect('/reg')
    elif len(request.form['lname']) <= 2:
        flash("Last name is blank")
        return redirect('/reg')
    elif len(request.form['fname']) <= 2:
        flash("First name is blank")
        return redirect('/reg')
    else:
        flash("Success! You are registured")   
    uname = request.form["uname"]
    email = request.form["email"]
    pword = md5.new(request.form["pword"]).hexdigest()
    fname = request.form["fname"]
    lname = request.form["lname"]
    query = "INSERT INTO users (`first_name`, `last_name`, `password`, `created_at`, `updated_at`, `user_name`, `email`) VALUES (:fname, :lname, :pword, now(), now(), :uname, :email);"
    data = {
             'uname':uname,
             'email':email,
             'pword':pword,
             'fname':fname,
             'lname':lname
            }
    user = mysql.query_db(query, data)
    return redirect('/user')

   

app.run(debug=True)