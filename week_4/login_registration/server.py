from flask import Flask, redirect, render_template,flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reg')
def regist():
    return render_template('registration.html')

app.run(debug=True)