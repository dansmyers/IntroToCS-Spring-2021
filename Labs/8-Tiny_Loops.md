# Short Loop Practice

## I Would Like to Say a Few Words

Write a program that uses a `while` loop to prompt the user to enter a word. Keep prompting until the user types one of the following words:

```
nitwit
blubber
oddment
tweak
```

## Thai 21

Here's a mathematical strategy game.

Beginning with a pile of 21 stones, players alternate removing stones until none are left. On her turn, a player may take 1, 2,
or 3 stones. The player who takes the last stone is the winner.

This game is known by a few different names, inluding the **Subtraction Game** and **Nim**. It was featured as a challenge 
on an episode of *Survivor: Thailand* where it was called **Thai 21**.

There are lots of variations:

- Changing the number of stones or the numbers that may be removed on each turn.
- Using multiple piles of stones. In classic Nim, a player may take as many stones as he wants, but from only one pile at a time.
- Playing a *misère* game (French for "destitution"), where the player who takes the last stone *loses*.

Write a program that implements the Thai 21 version of the Subtraction Game. Use the skeleton below to get started. You may assume that
the player always enters a valid number.

```
"""
Subtraction Game -- Thai 21 version
"""

stones = 21

playing = True

while playing:

    # Print the current number of stones
    print('Stones: %d' % stones)
    
    # Prompt player 1 to enter 1, 2, or 3
    print('Player 1')
    choice = int(input('Take 1, 2, or 3 stones: '))
    
    # Subtract the choice from the number of stones
    
    # If stones == 0, print a winning message and break to end the loop
    
        
    ### TODO: Write a similar block of code for Player 2's turn

```

## We Can Do Better

The game above plays fine, but is a little ugly because it uses almost identical code for both players. Use the code below to write another version of the 
Subtraction Game that has only a single block of turn-taking code. This version uses a variable called `player` to control whether it's player 1's turn or
player 2's turn.

At the end of the loop, check if the current player has won. If so, print a winning message and end the loop. If not, use an if-else statement to switch to the
other player.

```
"""
Subtraction Game -- Thai 21 version
"""

stones = 21
player = 1

playing = True

while playing:

    # Print the current number of stones
    print('Stones: %d' % stones)
    
    # TODO: Print the current value of player
    
    # Prompt player 1 to enter 1, 2, or 3
    choice = int(input('Take 1, 2, or 3 stones: '))
    
    # Subtract the choice from the number of stones
    
    # If stones == 0, print a winning message and set playing = False
    if stones == 0:
    
    
    # Else, switch to the other player
    else:
        # If player == 1, then set player = 2 and vice-versa

```


## Input Checking

What if we don't want to assume that the player will always enter 1, 2, or 3? We could use a `while` loop to force the player to give valid input.

```
getting_input = True

while getting_input:
    choice = int(input('Take 1, 2, or 3 stones: '))

    if choice < 1 or choice > 3:
        print('You must take 1, 2, or 3 stones.')
    else:
        getting_input = False
```

Modify your program to include the input-checking code and verify that you can force the user to input 1, 2, or 3. An even more sophisticated
version would check that the player's choice does not exceed the number of stones remaining in the pile.
