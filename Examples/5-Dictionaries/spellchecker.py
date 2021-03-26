"""
Spellcheker
"""

# Goal: write a program that uses the word list in words.txt to
# check the spelling of an input sentence
#
# Given a sentence, we want to break it into its component words
# then check if each word exists in the set of valid words
#
# If a given word is not present in the valid set, we'll assume
# that it's misspelled.
#
# Lots of variations on this idea are possible: Variant spellings,
# make suggestions, etc.

# Key idea: Dictionaries are very good for building a lookup set
#
# Strategy: Store the valid words as KEYS in a dictionary
#
# Python makes it very easy to test if a given key is contained in
# a dictionary and this lookup is very fast -- faster than iterating
# through a list to see if the list contains the key


def build_valid_word_set():
    
    valid_words = {}
    
    # Loop through the list of words
    f = open('words.txt', 'r')
    
    for line in f:
        line = line.strip()
        
        # Insert this word into the dictionary of valid words
        #
        # Each word is a KEY in the dictionary
        # In this case, the value mapped to the key is not important
        # Value can be anything
        # All we care about is doing fast lookups against the
        # set of words stored as keys
        
        valid_words[line] = ''
    
    return valid_words


def check_sentence(sentence, valid_words):
    
    # Break the sentence into its component words
    #
    # The built-in split method can separate a string
    # Default behavior is to split on whitespace
    # Result is a list of split out parts
    test_words = sentence.split()
    print(test_words)
    
    # Check each of those words to see if it exists in the spelling dict
    for w in test_words:
        w = w.lower()
        
        # Remove any punctuation marks that have been included with the word
        #
        # The replace string function will take out instances of a given
        # character and replace it with another character that you specify
        w = w.replace('.', '')
        
        if w not in valid_words:
            print(w)


### Main
spelling_dict = build_valid_word_set()


# Check the dictionary to see if it contains a word
#
# Use the in keyword
print('queueing' in spelling_dict)
print('cmputer' in spelling_dict)
