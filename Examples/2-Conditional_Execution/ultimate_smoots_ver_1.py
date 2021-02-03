"""
Final boss Smoots converter

Allow the user to choose feet-to-smoots vs. smoots-to-feet
and perform the appropriate conversion
"""

# 1. Print a welcome message
print('Welcome to the Ultimate Smoots Converter v0.01')

# 2. Print the menu of choices
print('1. Feet to Smoots')
print('2. Smoots to Feet')

# 3. Ask for the user's number
user_input = input('Enter your choice: ')
choice = int(user_input)

# 3.5 Check for valid input
# TODO: complete this part


# 4. Perform the appropriate conversion
FEET_PER_SMOOT = 5.5833

if choice == 1:
    # Feet to Smoots

    feet = float(input('Enter a number of feet: '))
    smoots = feet / FEET_PER_SMOOT
    print("That is %.2f smoots." % smoots)
    
else:
    # Smoots to Feet

    smoots = float(input('Enter a number of smoots: '))
    feet = smoots * FEET_PER_SMOOT
    print("That is %.2f feet." % feet)
