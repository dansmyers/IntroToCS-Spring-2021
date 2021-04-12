# Get Ye Flask

<img src="http://www.hrwiki.org/w/images/d/d9/Origin_of_ye_flask.PNG" width="50%" />

## Description

The goal of today's lab is to practice using the Flask framework and build a complete application. Along the way, we'll touch on:

- Serving a static HTML page.
- Receiving an input request from the client's web browser and passing it to the back-end.
- Creating the baby name popularity tracker that combines Flask and Pandas

## Review Flask

Change to your `Flask` directory and make a file named `app.py`. We're going to start with the code we wrote last time, then build up to a complete application. Put the following
code in `app.py`.

```
"""
Flask application
"""

from flask import Flask, request, Response

app = Flask(__name__)


### Each Flask route connects a function to a URL endpoint

@app.route('/hello')
def hello():
    return 'Hello, World!'
    
@app.route('/goodbye')
def goodbye():
    return '<h1>Goodbye, World!</h1>'
    
@app.route('/')
def index():
    return '<h1>This should be the index page.</h1>'
```

Recall the key idea of Flask (and web frameworks in general): **Every function provided by the app is connected to a URL endpoint**. When the client-side web browser sends a reques
