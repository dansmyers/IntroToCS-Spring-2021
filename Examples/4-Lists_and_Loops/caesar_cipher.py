"""
Implementation of the Caesar rotational cipher
"""

# Key ideas:
#
# Every text character has a corresponding numeric code. For example,
# 'A' corresponds to code 65.
#
# The built-in function ord() will return the code of a character
#
#     ord('A') ---> 65
#
# chr() will covert a numeric code to its associated character.
#
#     chr(65) ---> 'A'


def encrypt(plaintext, n):
    
    """
    Encrypt the plaintext message by rotating each letter n positions
    
    Assume plaintext is ALL CAPS with no spaces or punctuation.
    """
    
    # Empty string that will hold the ciphertext message
    output = ""
    
    # A string is a sequence of characters. Use the for loop
    # to iterate over the letters in the input message.
    for letter in plaintext:
        
        # Map the letter to the range 0-25
        code = ord(letter) - ord('A')
        
        # Shift by n positions, use mod to wrap around
        code = (code + n) % 26
        
        # Convert back to a letter
        code = code + ord('A')
        shifted_letter = chr(code)
        
        # Append to the output
        output += shifted_letter
    
    return output    
        
        
def decrypt(ciphertext, n):
    
    """
    Decrypt a message by rotating each letter back by n positions
    """
    
    # Process is identical to encryption except the value of
    # is subtracted from the letter code rather than added
    
    output = ""
    
    for letter in ciphertext:
        
        code = ord(letter) - ord('A')
        code = (code - n) % 256  # 
        code = code + ord('A')
        output += chr(code)

    return output


### Main
original_message = "ATTACKATDAWN"
print(original_message)

encrypted_message = encrypt(original_message, 3)
print(encrypted_message)

decrypted_message = decrypt(encrypted_message, 3)
print(decrypted_message)
