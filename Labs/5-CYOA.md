# Choose Your Own Adventure

## Description

If you had been a kid in the 80's, your elementary school library would have been stuffed with *Choose Your Own Adventure* books, for the downtime you had when you weren't playing [*Oregon Trail*](https://en.wikipedia.org/wiki/The_Oregon_Trail_(1985_video_game)) on your school's Apple II computers.

<img src="https://upload.wikimedia.org/wikipedia/en/f/f0/Cave_of_time.jpg" width="35%" />

Each book was the story of "you", the nameless protagonist, making your way through some type of fantastic adventure story. After reading for a few pages, you'd be offered a choice. For example,

- *If you choose to explore the mysterious Cave of Time, turn to page 41*.
- *If you would rather go back to your house and make a sandwich, go to page 17*.

Each choice would lead to a different path of the story and eventually you would reach an ending page, which might good, bad, or curiously ambiguous.

The CYOA books are part of the larger gaming lineage of **interactive fiction**. Some of the earliest PC games were structured as interactive stories, where the player types commands to move around the world, gather items, and solve puzzles. These early text-based IF games later evolved into graphical adventure games.

<img src="https://upload.wikimedia.org/wikipedia/en/a/ac/Zork_I_box_art.jpg" width="35%" />

*The Zork series published by Infocom was an influential early computer game. It is pitch black. You are likely to be eaten by a grue.*

We're going to use Python to write our own text-based Choose Your Own Adventure story. A key idea of this program will be **using functions to organize a complex program**. 
Each "page" of the story will be its own function. Within each function, print a little descriptive text, then prompt the user to make a choice. 
Each choice corresponds to another function call, which runs the code for the next page.

## Example

### Setup

```
cd CMS_120

mkdir Lab_5

cd Lab_5

touch cyoa.py

open cyoa.py
```

### Some Starter Code

Copy the following code in your `cyoa.py` file, then run it a couple of times to see how it works. Once you have played through a few paths, trace the execution of the source code and verify that you understand how it works.

```
"""
A Choose Your Own Adventure Story, featuring functions

CMS 120
"""

def read_choice():
    """
    Read and return an integer value
    """
    return int(input('Make a choice: '))
    

def go_to_house():
    
    print()
    print('Congratulations! You made back to your house!')
    print('If only there was some way to get inside...')
    print()
    
    # Add some more choices
    # Each choice corresponds to a function that represents the next page in the story
   
   
def read_leaflet():

    print()
    print('The leaflet turns out to be a coupon for a nearby all-you-can-eat buffet.')
    print('Your stomach rumbles...')
    print('But you need to head back to your house before you do anything else.')
    print()
    
    # Go directly to the next page without offering a choice
    go_to_house()

    
def open_mailbox():
    
    print()
    print('Opening the mailbox reveals a small leaflet.')
    print()
    
    print('1. Read the leaflet.')
    print('2. Change your mind and go to the house.')
    
    choice = read_choice()
    
    if choice == 1:
        read_leaflet()
    else:
        go_to_house()
        

def start():
    
    print()
    print('You are standing in an open field west of a white house with a boarded front door.')
    print('There is a small mailbox here.')
    print()
    
    print('1. Go to the house.')
    print('2. Open the mailbox.')
    
    choice = read_choice()
    
    if choice == 1:
        go_to_house()
    else:
        open_mailbox()
        
        
def print_instructions():
    
    print('Welcome to my Choose Your Own Adventure story!')
    print()
    
    print('Every page in this book is implemented as a function.')
    print('On each page, you\'ll make a choice, which calls the next function.')
    print('Let\'s begin!')
        
        
### Main
print_instructions()
start()
```

### Structure of the Program

The `main` part calls two functions: `print_instructions`, which just prints an intro message and then returns, and `start`, which is
the first page of the story.

The `start` function prints a little description of the scene and then prompts the user to choose option 1 or 2, reading the choice
with the `input` function.

Each choice corresponds to another function: `go_to_house` or `open_mailbox`. If the user makes choice 2, for example, the program calls the `open_mailbox` function, which represents another page in the story with another set of choices.

Here's a key idea: within `start`, we're using functions to **describe what should happen next**. Each function represents one self-contained page with calls to the functions representing other pages. Thus, the code is nicely compartmentalized. In particular, **we could change the code for one page without having to rewrite any other page**.

## Your Mission

Once you're comfortable with the basic example story, take control and write your own. You can use the starter code as a model and either keep the same opening scenario and choices or write something completely different.
Here's the basic plan:

- Use the `start` function as a model for all of your functions.

- Each function prints some text of the story, then prints some choices. You can do 1, 2, 3, or more choices, depending on how you want
the story to develop.

- Read the number for the user's choice with the `read_choice()` function. You can assume the user will always put in a valid number.

- For each choice, call a function that decribes what you want to happen next.

- Then go write those methods to create the next pages of the story.
