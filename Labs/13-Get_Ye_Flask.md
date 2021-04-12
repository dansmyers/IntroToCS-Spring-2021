# Get Ye Flask

<img src="http://www.hrwiki.org/w/images/d/d9/Origin_of_ye_flask.PNG" width="50%" />

## Description

The goal of today's lab is to practice using the Flask framework and build a complete application. Along the way, we'll touch on:

- Serving a static HTML page.
- Receiving an input request from the client's web browser and passing it to the back-end.
- Creating the baby name popularity tracker that combines Flask and Pandas

## Review Flask

Change to your `Flask` directory and make a file named `app.py`. We're going to start with the code we wrote last time, then build up to a complete application. Put the following code in `app.py`.

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

Recall the key idea of Flask (and web frameworks in general): **Every function provided by the app is connected to a URL endpoint**. When the client-side web browser sends a request over the Internet to a particular server URL, the Flask framework gets involved behind the scenes to run the associated Python function. Whatever is returned by the function is sent back to the client as a response.

To run the application, type

```
export FLASK_APP=app.py

flask run
```

This will bring up the Flask webserver, which you can view by going to `View ---> View Port ---> 5000`.

Add one more practice route to your app that returns a message and verify that you can visit all of the routes.

## Serve a Static Page

The app above returns a static message when the user first loads the page. Let's improve that by returning a real HTML page.

Start by creating the page. **Static pages must go in a special directory called `static`.

```
mkdir static

touch static/index.html

open static/index.html
```

Edit `index.html` to create a starting page. Here is a framwork to help you get started. Save your file when you're finished. Remember that you can use `<h1>`, `<h2>`, and `<p>` tags to give your page structure.

```
<!doctype html>
<html>
    <head>
        <title>TITLE GOES HERE.</title>
    </head>
    
    <body>
        <h1>EXAMPLE INDEX PAGE</h1>
        
        <p>Add content to the body.</p>
    </body>
</html>
```

Now update the index method of `app.py` to the following:

```
@app.route('/')
def index():
    return app.send_static_file('index.html')
```

And change the second line to identify the location of the static file directory.

```
app = Flask(__name__, static_url_path='', static_folder='./static')
```

If your server is still running, stop it by pressing CTRL + c. Then re-run the server and view port 5000 again. You should see the index page you created.

```
flask run
```

## Communication

To create interactive pages, we need the ability to pass information between the client-side and server-side of the application. There are a few different ways to do this, but here is the strategy that we'll employ:

- The front-end `index.html` defines input elements using the `<input>` tag. One of the elements will be a button that the user presses to submit a request.

- When the user clicks said button, it will trigger a little bit of JavaScript code embedded in `index.html` to collect any necessary input values and send a request off to the server.

- We can, optionally, augment this JavaScript with more features that take the server's response and process it for the front-end page.

**You don't need to write any client-side JavaScript**. I'll give you all of the front-end examples that you need. Our focus will be on understanding the Python code running on the server.

### Client-Side

Update `index.html` to the following:

```
<!DOCTYPE html>
<html>

    <!-- Head contains metadata on the whole document -->
    <head>
        <title>CMS 330 REST Demo</title>
    </head>

    <!-- Body contains the page's content -->
    <body>
        <h1>Input Example</h1>

        <p>Type your name in the box below and press Submit.</p>

        <input type="text" id="inputBox" />
        <button type="button" id="submitButton"> Submit </button>

        <!-- The div tag creates a named region of the page -->
        <div id="responseDiv"></div>

        <!-- script tag contains JavaScript that interacts with page elements -->
        <script>
            // Set a listener function for the button click
            document.getElementById('submitButton').onclick = function () {

                // Get the current string in the text box
                var input = document.getElementById('inputBox').value;

                // Create and send an HTTP request
                var oReq = new XMLHttpRequest();
                oReq.addEventListener("load", responseListener);
                oReq.open("GET", "/5000/hello?name=" + input);
                oReq.send();
            }

            // Listener runs when the server's response comes back
            function responseListener() {
                document.getElementById('responseDiv').innerHTML = this.responseText;
            }
        </script>
    </body>
</html>
```

Take a look at the code for a moment. It's more complicated than our previous pages, but you can identify a few elements:

- The tags that define an input textbox and the submit button.

- The `<div>` tag creates a "division" of the page. It doesn't do anything by itself, but can be used to identify a region of the page that might be manipulated by JavaScript code later. In our case, the `<div>` section will hold the server's response.

- The JavaScript code is in a `<script>` block.

- The script uses a built-in feature called `XmlHttpRequest` to send a request to the server.

The most important line of the JavaScript is this one:

```
oReq.open("GET", "/5000/hello?name=" + input);
```

The line specifies that the client's request should go to the `/hello` route on the server. As we have already seen, that's going to invoke a little bit of code associated with the `hello` route.

What's up with the `?name=` part? Here's a second key concept: **One way to pass information from a client to a server is to embed that information in the request URL**. The request parameters are passed after a `?` character and each parameter is identified by its name.


You can see this behavior. Go to google.com and perform a search, then look at the URL that's generated. You'll probably see something like:

```
https://www.google.com/search?q=pointy+guitars
```

Followed by a **lot** of other options that specify stuff about your browser, location, etc.

- `/search` is the Google endpoint to initiate a search request. When you send a request here, Google's back-end infrastructure kicks in to process the search and return the results page.

- `q=` is the search query term. In the case, it's actually two words joined together by a `+` symbol.

Take a moment and try manually constructing some Google queries by directly entering the search URL with a `q` parameter.

In our example, the parameter we're passing is called `name` and it has the value that the user typed in the input box, which was read out at the beginning of the script.

## Server-Side

Update your `hello` function to the following:

```
@app.route('/hello')
def hello():

    # Read the input name parameter
    name = request.args.get('name')
    
    return 'Hello, ' + name + '!'
```

The change here is small. Flask is smart enough to unpack the parameters included in the request URL (the `?name=` thing) and assign them to a `request` object. The first line of the function extracts the user's input name from `request`.

### Test

Re-run your app with `flask run` (again, stop the server with CTRL + c if you need to). Reload your index page, type your name in the box and press the button. You should see the response message appear below the box.

Experiment with changing the message returned by the server. **You must stop and re-run the server each time you make a change to `app.py`**.

## Baby Names

Believe it or not, we now have all of the pieces in place we need to write the complete baby name popularity program.

### Client-Side

Here is the complete `index.html` page. It's longer that the last example, but most of the extra length is in a big structure of options that are used by the Highcharts API to generate the plot. The important part of the app is almost exactly the same as the simple hello example: There are some inputs, a script the reads the values of the inputs, and then a request that goes to a server URL passing along the input values as parameters.

```
<!DOCTYPE html>
<html>
    
    
    <head>
        <style>
            body {
                font-family: "Arial", sans-serif;
                font-size: 16pt;
                color: #333333;
                background-color: #FEFEFE;
                margin: 40px auto;
                max-width: 800px;
            }
            
            input {
                font-size: 16pt;
            	padding: .25em .5em .25em .5em;
            	background-color: #FCFCFC;   
            }
        </style>
        
    </head>
    
    
    <body>
        <h1>Baby Name Popularity Tracker</h1>
        
        <figure class="highcharts-figure">
            <div id="container"></div>
        </figure>
        
        <label for="nameInputBox">Enter a name</label> <br>
        <input type="text" id="nameInputBox">

        <br><br>
        
        
        <input type="radio" id="female" name="sex" value="F" checked>
        <label for="female">Female</label><br>
        <input type="radio" id="male" name="sex" value="M">
        <label for="male">Male</label><br>
        
        <br>
        
        <input type="submit" id="button" value="Submit">
        
        <!-- JavaScript controls the page's behavior -->
        <script>
        
            //*** Submit function ***//
            //
            // This function runs when the user clicks the button
            document.getElementById('button').onclick = function() {

                // Use XMLHttpRequest to send an asynchronous request to the server
                var xmlhttp = new XMLHttpRequest();

                // This function runs when the server's response arrives
                xmlhttp.onload = function() {
                    // Parse the JSON response and extract rankings
                    let response = JSON.parse(this.responseText);
                    let rankings = response.data;
                    
                    createPlot(rankings);
                };
                
                // The name typed in the box
                let name = document.getElementById('nameInputBox').value;
                
                // The value of the selected radio button
                let sex;
                
                if (document.getElementById('female').checked) {
                    sex = 'F';
                } else {
                    sex = 'M';
                }

                // Format the URL to pass the parameters using HTTP GET
                xmlhttp.open("GET", "/5000/submit?name=" + name + "&sex=" + sex);
                xmlhttp.send();
            }
        
        
            //*** Create a plot from the server's response ***//
            //
            // Wraps around the Highcharts API
            function createPlot(data) {
            
                // Convert response data into a list of objects
                //
                // The 'low' parameter sets the bottom of the bar so it rises
                // from the bottom to the top of the reversed axis
                //
                // maxValue fixes the maximum ranking to 200 for consistently
                // popular names
                maxValue = Math.max(200, Math.max(...data) + 100);
                
                var rankings = [];
                for (i = 0; i < data.length; i++) {
                    rankings.push({'y': data[i], 'low': maxValue + 1});
                }
    
                // Array of year values
                years = [];
                for (let i = 1910; i < 2020; i++) {
                    years.push(i);
                }
                
                Highcharts.chart('container', {
                    chart: {
                        type: 'column'
                    },
                    title: {
                        text: 'Name Popularity by Year'
                    },
                    xAxis: {
                        categories: years,
                        crosshair: true,
                        tickInterval: 5,
                        
                        title: {
                            text: 'Year'
                        }
                    },
                    yAxis: {
                        min: 1,
                        max: maxValue + 1,
                        reversed: true,
                        endOnTick: false,
                        title: {
                            text: 'Rank in year'
                        }
                    },
                    plotOptions: {
                        column: {
                            groupPadding: 0.0,
                            pointPadding: 0.0,
                            borderWidth: 0.1
                        },
                        threshold: maxValue + 1
                    },
                    series: [{
                        name: 'Relative popularity',
                        data: rankings,
                        showInLegend: false
                    }],
                });
            }
            
        </script>
        
        
        <!-- Highcharts for histograms -->
    	<script src="https://code.highcharts.com/highcharts.js"></script>

        
    </body>
    
    
</html>
```

### Server-Side

Here is the complete `app.py` for the baby names server.

- Put the code in `app.py` and re-run the app.

- Once you are able to run the app, spend a few moments looking at the server code. Which parts do you recognize.

- **When you have gotten the app to work, come to me and I'll walk through the important parts of the code with you and explain what each part is doing**.

```
from flask import Flask, request, Response, render_template
import json
import pandas as pd

app = Flask(__name__, static_url_path='', static_folder='./static')


### Constants

MIN_YEAR = 1910
MAX_YEAR = 2019


### Flask routes

@app.route('/')
def root():
    return app.send_static_file('index.html')

    
@app.route('/submit')
def get_name_popularity():
    
    """
    Return the year-by-year popularity rankings for a given baby name
    and sex combination.
    
    Parameters
    ----------
    name: the baby name, passed as HTTP GET parameter in the URL
    sex: 'F' or 'M', passed as HTTP GET parmatere in the URL
    
    Returns
    -------
    JSON-formatted list containing the year-by-year popularity rankings
    for the given name-sex combination.
    """
    
    # Parse HTTP GET parameters
    name = request.args.get('name')
    sex = request.args.get('sex')
    
    # Extract year and rank in year for the given name-sex combination
    name_subset = babynames[(babynames['name'] == name) & (babynames['sex'] == sex)]
    name_years = name_subset['year'].tolist()
    name_ranks = name_subset['rank_in_year'].tolist()
    
    # Some names do not appear in all years
    #
    # Build the return list with a value of None for the years where
    # the given name does not appear
    result = []
    
    for year in range(MIN_YEAR, MAX_YEAR + 1):
        if year not in name_years:
            result.append(None);
        else:
            result.append(name_ranks.pop(0))
    
    # Return as JSON
    # Python None values are automatically parsed to JavaScript null
    return_object = {'data': result}
    return Response(json.dumps(return_object),  mimetype='application/json')


### Main -- runs when the app starts

# Load babynames.csv into a pandas dataframe
babynames = pd.read_csv('./data/babynames.csv', names=['sex', 'year', 'name', 'count'])

# Construct a column giving the rank within each year and sex for each name
#
# e.g. Mary is the #1 ranking name for girls in 1910
babynames['rank_in_year'] = babynames.groupby(['year', 'sex'])['count'].rank(ascending=False)
```


    
