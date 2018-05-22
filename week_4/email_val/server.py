from flask import Flask, redirect, render_template, session, request, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'Telamondo'
mysql = MySQLConnector(app, 'emaildb')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/email', methods=['POST'])
def email_val():
    if len(request.form['input']) < 1:
        flash("Email can not be blank")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['input']):
        flash("Not valid email")
        return redirect('/')
    else:
        flash("Success! Your email is {}".format(request.form['input']))
    email = request.form["input"]
    query = "insert into emails (email, created_at, updared_at) values(:email, now(), now())"
    
    data = {
             'email': email
            }
    emails = mysql.query_db(query, data)
    return redirect('/success')

@app.route('/success')
def email():
    query = "SELECT * FROM EMAILS"
    emails = mysql.query_db(query)    
    return render_template('success.html', all_emails= emails)

@app.route("/success/delete/<email_id>")
def delete(email_id):
    query = "DELETE FROM emails WHERE id = :specific_id;"
    data = {
        "specific_id":email_id,
    }
    emails = mysql.query_db(query, data)
    return redirect("/success")



app.run(debug=True)


"""
Index
A simple form for the user to submit an email.
Error
If the email address is not valid, have a notification "Email is not valid!" to display on the homepage.
success.html
Once a valid email address is entered, save to the database the email address the user entered.
 On the success page, display all the email addresses entered along with the date and the time
 (e.g. June 24th, 2013, 6:00 PM) when the email addresses were entered
Bonus
Add a delete button onto your success page that allows the user to delete entries from the
 database from the success page. With the bonus feature added, your app should look a little different than above!"""