"""
Write a program that can print pyramids of stars

    *
   ***
  *****
 *******
*********

Use a variable to control the height of the pyramid. Example has a height of 5 lines.

First line has 1 star and 4 spaces
Second line has 3 stars and 3 spaces
Third line has 5 stars and 2 spaces
Fourth line has 7 stars and 1 space
Fifth line has 9 stars and 0 spaces
"""

height = 50

# Define vars for the number of spaces and stars on each line
num_stars = 1
num_spaces = height - 1

# Use a loop with the range function to execute height total times
for h in range(height):
    
    # Print the spaces and stars for the current line
    #
    # Use string multiplication
    # end='' prevents print from automatically moving to the next line
    print(' ' * num_spaces, end='')
    print('*' * num_stars)
    
    # Adjust num_spaces and num_stars for the next line
    num_spaces -= 1
    num_stars += 2
