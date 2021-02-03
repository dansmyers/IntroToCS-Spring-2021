"""
Write a menu-based affirmation program
"""

# 1. Print a welcome message and the menu of options
print('Welcome to the computer therapist.')
print('How are you feeling today?')
print('1. Happy')
print('2. Sad')
print('3. So-so')
print('4. Angry')


# 2. Read the user's choice
user_input = input('Enter the number of your choice: ')
choice = int(user_input)


# 3. Select a response message based on that choice
if choice == 1:
    print('You are happy.')
    print('That is great.')
elif choice == 2:
    print('You are sad.')
    print('Have you talked to a real person?')
elif choice == 3:
    print('You are so-so.')
    print('We all feel that way sometimes.')
elif choice == 4:
    print('You are angry.')
    print('Do not keep it bottled up inside yourself.')
else:
    print('That is not a choice.')
    print('But human feelings are complex.')
    
print('Goodbye.')
