## Variable parameters
## Jinja2 Template engine
## Build url dynamically

# Jinja2 Template engine
'''
{{ }} - expression to print output in HTML
{%...%} - control statements
{#...#} - comments 
'''
from flask import Flask, render_template, request, redirect, url_for

# WSGI application
app = Flask(__name__)

@app.route('/')
def function():
    return "<html><h1>This is a Simple Flask Application. THis is a Home Page<h1></html>"

@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"This is {name}."
    return render_template('form.html')

## variable parameters by default string
# @app.route('/success/<int:score>') # <int:score> is a variable parameter
# def success(score):
#     return f"Your score is {score}"


@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score >= 50:
        res = "Passed"
    else:
        res = "Failed"
    return render_template('result.html',result = res)

@app.route('/successres/<int:score>')
def successres(score):
    res = ''
    if score >= 50:
        res = "Passed"
    else:
        res = "Failed"
    exp = {'result': res, 'score': score}
    return render_template('result1.html',result = exp)

# if condition
@app.route('/ifcondition/<int:score>')
def ifcondition(score):
    return render_template('ifcondition.html', result = score)

@app.route('/submit1',methods=['GET','POST'])
def submit1():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        datascience= float(request.form['datascience'])
        C = float(request.form['C'])
        total_score = (science + maths + datascience + C) / 4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres', score = total_score))
        



# Entry point for the application
# This is the main function that runs the Flask application
if __name__ == '__main__':
    app.run(debug = True) # debug = true helps to reload the server automatically when code changes