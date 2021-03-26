"""
Estimate letter frequencies using the word list
"""

f = open('words.txt', 'r')

counts = {}

for line in f:
    line = line.strip()  # Strip extra whitespace
    
    # Iterate through the letter in the line
    for letter in line:
        
        # Use a dictionary to keep a count of the occurrences
        # of each letter
        
        # Special case to initialize the count for each letter
        # the first time it appears
        if letter not in counts:
            counts[letter] = 0
        
        counts[letter] += 1
        
        
# Loop over the keys and print each pair on its own line
#
# The for loop iterates over the keys in a dictionary
#
# In many cases, the ordering is the order in which the
# keys were inserted
#
# You should not assume any particular ordering on the keys
# that come out of a dictionary
for letter in counts:
    print(letter, counts[letter])
