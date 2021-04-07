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
