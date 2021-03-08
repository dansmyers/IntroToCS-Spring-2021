"""
Prompt the user to enter a string and echo back whatever the user types

Key idea: use the while loop to write a program that runs for an indeterminate
amount of time -- until some stopping condition is achieved
"""

looping = True

while looping:
    user_input = input('Say something: ')
    
    print(user_input)

    if user_input.lower() == 'stop':
        looping = False
