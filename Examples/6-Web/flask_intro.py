"""
Basic routing using the flask framework

Use the following commands to run:

export FLASK_APP=flask_intro.py

flask run
"""

from flask import Flask, request, Response, render_template

app = Flask(__name__, static_url_path='', static_folder='./static')


### Flask routes
#
# Each route is a URL endpoint associated with a Python function
#
# When the client sends an HTTP request to a URL, the flask framework
# runs that URL's associated code
#
# Any value returned by the function is sent back to the client as
# the HTTP response message

@app.route(‘/hello’)
def hello():
    return ‘Hello, World!’

@app.route('/')
def root():
    return app.send_static_file('index.html')


