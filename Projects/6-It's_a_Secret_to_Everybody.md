# Assignment 6: It's a Secret to Everybody

## Due Wednesday, March 31

## Submit your code to the assignment I'll create on Canvas

## Description

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c2/Danc-01.jpg" width="33%" />

Sir Arthur Conan Doyle wrote "The Adventure of the Dancing Men" in 1905. In it, Sherlock Holmes receives a request for help from a man whose wife has been receiving strange messages. The notes appear to contain only drawings of dancing stick figures, but leave her inexplicably terrified.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Dancing_men.svg/692px-Dancing_men.svg.png" width="50%" />

Holmes realizes that the stick men are actually a code. Each different figure corresponds to one letter of the alphabet and the flags mark the boundaries between words. Holmes breaks the code and learns the truth...which you'll have to learn for yourself by reading the story

The Dancing Men are an example of a **substitution cipher**: one of the simplest techniques for encoding secret messages. In this scheme, each letter in the **plaintext message** is mapped to a different letter of the alphabet (or another symbol, as in the Dancing Men) to yield the **ciphertext message**. Knowing the substitutions allows the encryption to be reversed.

For example,the coded message `GHHGDB GH EGJM` could be deciphered as `ATTACK AT DAWN` by substituting

- A for G
- T for H
- C for D
- K for B
- D for E
- W for J
- M for N.

Although substitution ciphers are easy to implement, they are insecure, because they’re vulnerable to **frequency analysis attack**. This is the method Holmes uses to break the Dancing Men cipher in the story.

The letters of English words are not randomly distributed: *e* is the most common (about 13% of occurrences), followed by *t* (9%) and then *a* (8%). Letters *q* and *z* each account for less than 1% of occurrences in common English text.

Therefore, given a large body of text that’s been encoded using a substitution cipher, the most frequently occurring letter is likely to be *e*, with the second most frequently occurring *t*, and so forth. Even when the correspondence between encrypted and decrypted letter frequencies is not exact, frequency analysis often yields enough information about the message to make decryption possible.

In this project, your mission is to use frequency analysis to decipher a message that I’ve encoded using a substitution cipher. Use frequency analysis to determine the letter frequencies in the enciphered text. Then, using a table of standard English letter frequencies, decrypt the ciphertext to produce the plaintext output.

## Getting the Input File

The enciphered message is in the file `cipher.txt` posted to Canvas. It contains the opening text of a famous work of literature. The punctuation, spaces, and capitalization of the text have been left intact and both capital and lowercase letters have been encrypted using the same substitutions.

Download the file from Canvas, then import it into your Mimir workspace by going to `File --> Upload`. Once you've uploaded the file, it will appear in your Mimir top-level home directory. You can move it to your `CMS_195/Dictionaries` project directory using

```
mv ~/cipher.txt ~/CMS_195/Dictionaries
```

Here, the `~` (tilde) symbol is a shortcut that represents your home directory and `mv` is the file move command.


## Tips

<img src="https://objects-us-east-1.dream.io/secrettoeverybody/images/secret.png" width="50%" />

You probably want to write two programs, one to do the frequency analysis and one to do the decryption. The frequency analysis program needs to scan the text file and count the occurrences of each letter character. Use the letter-counting example from the video on Canvas as a starting point.

The decryption program can read each character in the encrypted input, then look up a translation for that letter and output the translated character to produce the decrypted output. Use a dictionary to store mappings from one character to another.

The frequency analysis results may not be perfect, so you may need to apply a little reasoning and experimentation to get the complete translation.

You can use the string's `.lower()` method to convert a line to all lowercase letters:

```
# Example of converting text to lower case

str = 'HELLO ,WORLD.'
str.lower()
print(str)  # prints 'hello, world.'
```
