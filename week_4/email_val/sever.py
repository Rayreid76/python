from flask import Flask, redirect, render_template, session, request
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'Telamondo'
mysql = MySQLConnector(app, 'EmailDB')

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/email', methods=['POST'])
def create():
    query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
    data = {
             'email': request.form['email'],
           }
    mysql.query_db(query, data)
    return render_template('success.html')
def email_val():
    quary = "SELECT * FROM EMAILS"
    emails = mysql.query_db(quary)
    print(emails)
    return render_template('success.html', all_emails= emails)

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