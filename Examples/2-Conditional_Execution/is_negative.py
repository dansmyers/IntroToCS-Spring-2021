"""
Test if an input number is negative
"""

user_input = input('Type a number.')
value = int(user_input)

if value < 0:
    print('Negative.')
else:
    print('Non-negative')
    
print('Done.')
