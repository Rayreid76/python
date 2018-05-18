from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'hotdog'


@app.route('/')
def index():
    if "name" not in session:
        session['name'] = []
    return render_template("index.html",)

@app.route('/results', methods=['POST'])
def create_results():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    else:
        session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['lang']
    if len(request.form['comments'])>120:
        flash("Please shorten your comments to 120 characters.")
        return redirect('/')
    else:
        session['comments'] = request.form['comments']
    return render_template('results.html', name=session['name'], location=session['location'], language=session['language'], comments=session['comments'])


app.run(debug=True)

"""Take the Dojo Survey assignment that you completed previously and add validations! The Name and Comment fields should be validated so that they are not blank. Also, validate that the comment field is no longer than 120 characters.
"""