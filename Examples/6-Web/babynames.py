"""
Local non-web based version of the babynames app
"""

import pandas as pd

### Main -- runs when the app starts

# Load babynames.csv into a pandas dataframe
babynames = pd.read_csv('./babynames.csv', names=['sex', 'year', 'name', 'count'])
print(babynames.head())

# Construct a column giving the rank within each year and sex for each name
#
# e.g. Mary is the #1 ranking name for girls in 1910
#      John is the #1 ranking name for boys in 1910
babynames['rank_in_year'] = babynames.groupby(['year', 'sex'])['count'].rank(ascending=False)


# Read a name and sex from the input
name = input('Enter a name: ')

print('1. Female')
print('2. Male')
user_input = int(input('Select sex: '))

if user_input == 1:
    sex = 'F'
else:
    sex = 'M'


# Select the subset of the dataframe matching the given name and sex
# Note: You must use & to combine two tests in Pandas
subset = babynames[(babynames['name'] == name) & (babynames['sex'] == sex)]


# Print the list of year-rank pairs
years = subset['year'].tolist()
ranks = subset['rank_in_year'].tolist()

for i in range(len(years)):
    print(years[i], ranks[i])
