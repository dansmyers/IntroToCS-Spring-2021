"""
Abbreviated version of the even-odd dice program (cho-han)
Roll two dice, add their sum, check if the result is even or odd
"""

roll two dice, add their sum, check if the result is even or odd

from random import randint

### Functions

def die_roll():
    """
    "Wrapper" method that uses a simpler name to surround
    a  more complicated function call
    """
    
    return randint(1, 6)


def sum_of_two_dice():
    return die_roll() + die_roll()
    
    
### Main

total = sum_of_two_dice()
print(total)

if total % 2 == 0:
    print('Even')
else:
    print('Odd')
