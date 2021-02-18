"""
Chuck-a-Luck

CMS 195, Spring 2020
"""

from random import randint

def read_int():
    """
    Read and return an integer from the terminal
    """
    
    # Write code to read a value with input(), then convert it to an int and return it
    return int(input('Enter a number 1-6: '))
    
  
def die_roll():
    """
    Generate and return a six-sided die roll
    """
    
    # Fill in the body of the method
    return randint(1, 6)


def print_instructions():
    """
    Instructions for the chuck-a-luck game
    """
    
    # Print instruction messages for the user
    # This method doesn't return anything
    
    print('Welcome to Chuck-a-Luck.')
    print('Choose a number 1-6 and roll three dice.')
    print('You win the number of dollars equal to the number of times your choice comes up')
    
    
### Main
    
print_instructions()

# Read the user's bet
bet = read_int()

# Generate three dice
die1 = die_roll()
# Use die_roll() to initialize variables die2 and die3
die2 = die_roll()
die3 = die_roll()

print('The dice are %d, %d, and %d.' % (die1, die2, die3))
    
# Count up the number of dice that match the user's bet
# Tip: create a count variable and test each die with an if statement

count = 0

if die1 == bet:
    count = count + 1

if die2 == bet:
    count = count + 1

if die3 == bet:
    count = count + 1

# Print the outcome
print('You win $%d.' % count)
