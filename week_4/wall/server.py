from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import MySQLConnector
import md5
app = Flask(__name__)
app.secret_key = 'grantspass'
mysql = MySQLConnector(app, 'rays_wall')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wall')
def wall():
    user = mysql.query_db("SELECT * FROM users where id = {}".format(session["user_id"]))[0]
    posts = mysql.query_db("SELECT *, posts.id as post_id FROM posts join users on users.id = posts.users_id;")
    comments = mysql.query_db("select *, comments.id as comment_id from comments join users on users.id = comments.user_id;")
    return render_template('wall.html', user=user, posts=posts, comments=comments)

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
            "email":request.form["user_name"],
            "password":md5.new(request.form["password"]).hexdigest()
        }
        users = mysql.query_db(query,data)
        return redirect('/wall')

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
    else:
        query = "select * from users where users.email = :email and users.password = :password"
        data = {
            "email":request.form["user_name"],
            "password":md5.new(request.form["password"]).hexdigest()
        }
        users = mysql.query_db(query,data)
        if len(users)>0:
            user = users[0]
            session["user_id"] = user["id"]
        return redirect('/wall')

@app.route('/wall/post', methods=['POST'])
def message():
    value = True
    if request.form["message"] == "":
        value = False
        flash("There is no message to post.")
    else:
        query = "INSERT INTO posts (`users_id`, `message`, `created_at`, `updated_at`) VALUES (:user_id, :message, now(), now());"
        data = {
            "user_id":session["user_id"],
            "message":request.form["message"]
        }
        posts = mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/wall/<post_id>', methods=['POST'])
def comment(post_id):
    value = True
    if request.form["comment"] == "":
        value = False
        flash("There is no comment to post.")
    else:
        query = "INSERT INTO `comments` (`user_id`, `post_id`, `comment`, `created_at`, `updated_at`) VALUES (:user_id, :post_id, :comment, now(), now());"
        data = {
            "user_id":session["user_id"],
            "post_id":post_id,
            "comment":request.form["comment"]
        }
        comments = mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/logoff')
def logoff():
    session.clear()
    return redirect('/')


app.run(debug=True)

"""Create a wall/forum page where users will be able to post a message and see the message displayed by other users. Store the messages in a table called 'messages' and retrieve the messages from the database. Follow the below wireframe.

1. Create a login and registration page that is displayed when a user navigates to 'localhost:5000/'

2. Once the user has logged in successfully redirect them to 'localhost:5000/wall' that will show the wall.

Download the handout for the wireframe/ERD:"""