from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def tmnt():
    return render_template('ninja.html')

@app.route('/result', methods=['POST'])
def results():
    color = request.form['color']
    if color == 'blue':
        print(color)
        return render_template('result.html')
    elif color == 'red':
        return render_template('rap.html')
    elif color == 'orange':
        return render_template('mich.html')
    elif color == 'purple':
        return render_template('don.html')
    else:
        return render_template('no_ninja.html')

app.run(debug=True)