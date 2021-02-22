"""
Thinking about constants as a global variable
"""


### Key ideas:
#
# Variables defined OUTSIDE OF A FUNCTION (in the "main" part of the program) are GLOBAL
#
# Global variables are visible from INSIDE ANY FUNCTION in the same script
#
# Global variables are useful for defining constants, like FEET_PER_SMOOT in this example, or pi
#
# DO NOT USE GLOBAL VARIABLES TO PASS INFORMATION BETWEEN FUNCTIONS
#
# Functions should take input through their parameters and return values using the return statement
#
# Global variables create a "side channel" that allows data to change in ways the programmer may not have intended


FEET_PER_SMOOT = 5.5833


def feet_to_smoots(feet):
    return feet / FEET_PER_SMOOT
    

def smoots_to_feet(smoots):
    return smoots * FEET_PER_SMOOT
    

### Main
value = float(input('Enter a number of feet: '))

print('That is %.2f smoots.' % feet_to_smoots(value))
