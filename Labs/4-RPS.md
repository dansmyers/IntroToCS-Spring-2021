## Rock-Paper-Scissors

### Overview
This section will lead you guide you through the implementation of an RPS game. This program will tie together pretty much everything that we've done so far in the class:

- Printing
- Variables
- User input
- Relational operators
- Conditional execution
- Randomness
- Logical operations

This version of the game will play one round of human vs. computer. A little later, we can talk about how to modify the program to play something like best two-out-of-three.

Here's an example play session.

```
Welcome to Rock, Paper, Scissors.
1. Rock
2. Paper
3. Scissors
Select your move:
1
Rock. A strong choice.
BEEP BOOP I CHOOSE SCISSORS.
ROCK CRUSHES SCISSORS!
MY FAILURE...DOES NOT COMPUTE...
```

### Setup

```
cd CMS_120

mkdir Lab_4

cd Lab_4

touch rps.py

open rps.py
```

### Starting Code

Use the code below as a starting point. Each of the sections below will ask you to add a new part to the skeleton program.

```
"""
A Rock-Paper-Scissors game that plays one round of human vs. computer

CMS 120
"""

# Imports
from random import randint
import sys

# Declare constant variables representing the three moves

# Print the welcome message and list the three moves

# Read the user's move

# If the move is not 1, 2, or 3, exit the program

# Randomly generate the CPU's move using randint

# Print a string representing the CPU's move

# Determine the outcome and print a message

```

### Step 1: Declare Constants
We have to decide how to represent the player's and computer's moves. There are many different ways to do this. We could, for example, 
have the player type in a string for the chosen move, like "Rock". This approach could work, but we'd have to deal with the complexity 
of raw text input.

A more structured approach is to assign each move a number. Now, we can read the user's move by prompting him or her to type 1, 2, or 3 and generate the computer's move by picking a random value 1, 2, or 3.

Add three lines mapping the three moves to the numbers 1, 2, and 3:

```
ROCK = 1
PAPER = 2
SCISSORS = 3
```

Now you can use the name ROCK in your program instead of always remembering "1 stands for rock."

### Aside: Constants

Recall that variables named with ALL CAPS are considered to be **constants**: the value of a constant variable **should not change** after its first assignment.

The use of ALL CAPS names to indicate constants is a **convention** of Python programming, not a rule. Other languages, like Java, have ways to declare constants that literally cannot change: the Java compiler will generate an error if you attempt to modify a constant variable.


### Step 2: Print the Welcome Message and List the Three Moves
Add four print statements that print the opening text for the game.

```
Welcome to Rock, Paper, Scissors.
1. Rock
2. Paper
3. Scissors
```


### Step 3: Read the Player's Move
Prompt the player to select one of the moves and read the response using `input`.

```
player_move = int(input('Select your move: '))
```


### Step 4: Check for Valid Input
The only legal moves are 1, 2 or 3. Add some code to check if the user enters a value outside that range, and if so exit the program.

```
if player_move < 1 or player_move > 3:
    print('That is not a valid move.')
    sys.exit()
```


### Step 5: Print the Player's Move
Add an `if-elif-else` block that tests the player's input and prints the associated move.

```
if player_move == ROCK:
    print('Rock. A strong choice.')
```

Add two more cases for PAPER and SCISSORS.

### Step 6: Randomly Generate the CPU's Move
Write a line that uses `randint` to generate a 1, 2, or 3 and save it into a variable named `cpu_move`.

```
cpu_move = randint(1, 3)
```

### Step 7: Print the CPU's Move
Add another `if-elif-else` block to print a message for each possible computer move.

```
if cpu_move == ROCK:
    print('BEEP BOOP I CHOOSE ROCK.')
```

Add two more cases for PAPER and SCISSORS.

### Step 8: Determine the Outcome
This is the most complex part. You need to write a set of conditional statements that will compare the player and CPU moves and print the appropriate outcome message.

One case is easy: if the moves are the same, it's a draw.

```
if player_move == cpu_move:
    print('DRAW. I WILL GET YOU NEXT TIME HUMAN.')
```

Now add more statements to test for the other possible combinations. For example,

```
if player_move == ROCK and cpu_move == PAPER:
  print('PAPER COVERS ROCK.')
  print('HUMANS...SO SOFT...SO WEAK.')
```
