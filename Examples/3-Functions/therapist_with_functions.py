"""
A version of the menu-based therapist with randomized responses

Key idea: illustrate the stepwise refinement technique for developing
programs using functions
"""

### Stepwise refinement
#
# Start with the high-level goal of the program
#
# Write down a series of high-level steps that will accomplish
# the goal of the program
#
# Write a function to implement each high-level step
#
# As you implement each sub-task level function, decide
# if that function can be implemented directly as code or
# if it should be broken down into further subtasks


from random import randint

def print_welcome_and_menu():
    print('Welcome to the therapist.')
    print('Select one of the emotional options below.')
    print('1. Happy')
    print('2. Sad')
    print('3. Indifferent')


def read_choice():
    user_input = input("Enter your choice: ")
    return int(user_input)


def print_happy_message():
    r = randint(1, 3)
    
    if r == 1:
        print('That is great.')
    elif r == 2:
        print('That is splendid.')
    else:
        print('I am elated to hear that.')
        

def print_sad_message():
    r = randint(1, 3)
    
    if r == 1:
        print('I am sorry to hear that.')
    elif r == 2:
        print('Sadness is a valid part of the emotional spectrum.')
    else:
        print('Practice self care.')
        
        
def print_indifferent_message():
    r = randint(1, 3)
    
    if r == 1:
        print('Eh.')
    elif r == 2:
        print('I understand. I also cannot even.')
    else:
        print('Practice self care.')
        
def print_error_message():
    print('That is not a choice, but the emotional spectrum is complex.')
        

def print_randomized_response(value):
    
    # If the use chose happy, print a random happy message
    if value == 1:
        print_happy_message()
    
    # Else if the user chose sad, print a random sad message
    elif value == 2:
        print_sad_message()
        
    # Else if the user choce indifferent, print a random indifferent message
    elif value == 3:
        print_indifferent_message()
     
    # Default else: print an error message  
    else:
        print_error_message()
    
    

# 1. Print the welcome message and the menu of emotional options
print_welcome_and_menu()

# 2. Read the user's choice
choice = read_choice()

# 3. Print a randomized response based on the user's choice
print_randomized_response(choice)
