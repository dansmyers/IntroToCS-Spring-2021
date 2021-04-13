# Final Project

## Due Friday, April 30 (the day of our scheduled final exam)

## You can work with allies to complete your project. If you work with others, include their names in your project submission.

## Description

This is it, the final project.

**Make anything you want**, as long as it's awesome and uses the Python features that we've learned over the course of the semester.

Most of you will probably want to make some sort of game, but note that isn't required. You can make a text-based program, or a program that's more calculation-oriented if that's what you want.

## Requirements

1. Awesomeness.

2. Uses basic features of Python: variables, loops, conditional
   statements and functions. Almost any reasonably complex program is
   going to satisfy these requirements. If your program doesn't
   include most of these features then it might be too simple.
   
3. Uses at least one advanced data organization feature: a list,
   classes, or a dictionary. I'm not requiring any
   particular number of these, because the best choice depends on
   the nature of your program.
   
4. Demonstrates good programming style (indentation, variable names)
   and includes descriptive comments explaining what's happening
   in the program.
   
   
## Grading

Submit your Python code, including a brief description of the program in its docstring, to
Canvas. I'll run your program and look at the source code. I'll be checking:

1. Does it work? Even if it's simple, I want to see something that
   could be considered a complete working program, not an incomplete
   fragment.

2. Does it use the features of Python that we've discussed?

3. Does it follow good coding style, as we've used in class and in
  labs?

I'll mark each one of these three areas on a four point scale:

- 0 (not functional): doesn't run, uses no features, impossible to understand
    
- 1 (needs improvement): a working program with minimal functionality
         code is not clean, but is legible
 
- 2 (satisfactory): a complete working program that meets its stated goals
         code is well-formatted and has some comments
    
- 3 (excellence): a program that is both complete and demonstrates creativity
         incorporates one or more unique features
         code is well-formatted and has excellent documentation

I'll add up your 0-4 point scores in each of the three areas 
(completeness, use of Python, code style). You need to achieve
at least **six out of nine** points to earn satisfactory credit for
the entire project. Five or fewer points will result in an 
unsatisfactory grade.


## Tips

- **Start early**! Don't wait until the last minute!

- Start with the simplest idea that could work, get it to work, then
build up from there. It's better to have a complete program that does
what it's supposed to do than an ambitious but incomplete idea.

- Use the examples from our previous labs. They illustrate many different examples that could be useful
for your own programs.

## Ideas

### Interactive Fiction

Build a more complex interactive fiction game like the one we did in our lab early in the semester. Use functions to code each
page of the game.

You can use variables to keep track of information about the world or the player's actions. Even better: use a dictionary to keep track 
of state information for the game.

```
def example_page(state):
    """
    state is a dictionary that keeps track of information about the world or the player.
    """
    
    print("You see a key nearby.")
    print("1. Take the key.")
    print("2. Give up and go home.")
    choice = input("What shallst thou deaux?")
    
    # If the user chooses, set a variable in the state dictionary
    if choice == 1:
        state['has_key'] = True
        
    # Call another function to move to the next page
    next_page()
```

Later, you can check if `state['has_key']` is `True` to determine if the player has the ability to unlock a chest or door.

You would probably want an initialization function that sets up and returns the initial dictionary with default values
for every variable you intend to track in the game.

### Card Games

Use the object-oriented deck of cards to build a game. War is relatively easy and Blackjack is also a good choice. Poker is hard because
of the complexity of identifying and scoring the hands, so I don't recommend trying it unless you want an extra challenge.

### Nim

You might remember the Thai 21 game from one of our labs.

- Start with a pile of 21 stones.
- On her turn, a player may take 1, 2, or 3 stones from the pile.
- The player who takes the last stone is the winner.

Nim is a generalization of this game. There are variants, but here's a standard setup:

- Start with three piles of 20 stones each.
- A player may remove any number of stones on his turn, but from only one pile.
- The player who takes the last stone **loses**.

### Pig

A classic game played with one die. The object is to be the first player to accumulate 100 total points.

On your turn, roll the die.

- If you roll a 1, your turn ends immediately and you earn no points.

- If you roll any other number, add it to your points for this turn.

- You can then choose to either end your turn and add your accumulated points to your total score, or roll again to try and accumulate
more points for the turn.

- You can keep rolling as many times as you want to accumulate points before ending your turn, but if you roll a 1 your turn ends
immediately and you score no points for this turn. The strategy of Pig is trading off the risk of rolling a 1 vs. the benefit
of rolling repeatedly to get as many points as possible.
