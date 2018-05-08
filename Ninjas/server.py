from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def tmnt():
    return render_template('ninja.html')

app.run(debug=True)