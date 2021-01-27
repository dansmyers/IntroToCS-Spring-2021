# Lab 2 &ndash; Variables and Input

## Setup

Start your Mimir workspace. Change to your `CMS_120` directory and make a new directory called `Lab_2`.

```
cd CMS_120

mkdir Lab_2

cd Lab_2
```

To create each file use `touch`, then use `open` to open it in the editor.

```
touch magic_computers.py

open magic_computers.py
```

## The Magic Computers

<img src="https://miro.medium.com/max/2100/1*8M2JfaTacGjI8YQlO9qF5A.jpeg" width="50%" />

Mad Libs are a word completion game originally invented in 1953 by two New Yorkers, Leonard Stern and Roger Price, who went on to publish a series of best-selling books based on
the concept.

Each Mad Lib is an incomplete short story, where some of the words have been replaced by blanks, each labeled with a part of speech. One player asks the others for words
to fill in the blanks, then reads the complete story. Hilarity ensues.

Write a program to implement the "Magic Computers" Mad Lib given above. Use the input function to prompt the user to enter words of each type, then combine all of the
answers together to print the finished story. Here's a little bit to help you get started:

```

"""
The Magic Computers: a Mad Lib
"""

# Prompt the user to enter all of the required words
noun1 = input('Enter a noun: ')
plural_noun1 = input('Enter a plural noun: ')

# Add more cases for the other blanks...

# Print out the story with the user's words mixed in
# %s is the format specifier for a string variable
# This is an easy way to mix string variables in with other output
print('Today, every student has a computer small enough to fit into his %s.' % noun1)
print('He can solve any math problem by simply pushing the computer\'s little %s.' % plural_noun1)

# Add more print statements for the rest of the story...
```


## The Weight

<img src="https://staticg.sportskeeda.com/wp-content/uploads/2016/08/1-1470306645-800.jpg" width="50%" />

Write a program to read in a weight in kilograms and convert it to pounds. There are about 2.20462 pounds in one kilogram.
Display the result to one decimal place.

The current world record for weight lifted overhead in the clean and jerk is 263.5 kg, held by Iranian superheavy
weightlifter / human vending machine [Hossein Rezazadeh](https://www.youtube.com/watch?v=FOE-PZJq2sk):

Use your program to calculate the weight of Rezazadeh's record lift in pounds.


