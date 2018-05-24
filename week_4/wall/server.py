from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = 'grantspass'
mysql = MySQLConnector(app, 'rays_wall')
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration', methods=['POST'])
def create():
    value = True
    if request.form["user_name"] == "":
        value = False
        flash("error in Email")
    if request.form["password"] == "":
        value = False
        flash("error in Password")
    if request.form["name"] == "":
        value = False
        flash("error in Name")
    if value != True:
        return redirect('/')
    else:
        query = "INSERT INTO `users` (`name`, `email`, `password`, `created_at`, `updated_at`) VALUES (:name, :email, :password, now(), now());"
        data = {
            "name":request.form["name"],
            "email":request.form["email"],
            "password":request.form["password"]
        }
        mysql.query_db(query,data)
        return render_template('wall.html')

@app.route('/login', methods=['POST'])
def signin():
    value = True
    if request.form["user_name"] == "":
        value = False
        flash("error in Email")
    if request.form["password"] == "":
        value = False
        flash("error in Password")
    if value != True:
        return redirect('/')
    return render_template('wall.html')

app.run(debug=True)

"""Create a wall/forum page where users will be able to post a message and see the message displayed by other users. Store the messages in a table called 'messages' and retrieve the messages from the database. Follow the below wireframe.

1. Create a login and registration page that is displayed when a user navigates to 'localhost:5000/'

2. Once the user has logged in successfully redirect them to 'localhost:5000/wall' that will show the wall.

Download the handout for the wireframe/ERD:"""