from flask import Flask, render_template

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

# Entry point for the application
# This is the main function that runs the Flask application
if __name__ == '__main__':
    app.run(debug = True) # debug = true helps to reload the server automatically when code changes