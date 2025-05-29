3-Player Rock, Paper, Scissors: "Beat Geet" Edition

##  Who is this program for?
This is a fun and beginner-friendly project for anyone just learning Python. It's made for students who want to use basic lists, loops, and functions.

##  What does the program do?
The program randomly generates a move (rock, paper, or scissors) for 3 players using your own function `move()`, then decides who wins based on the rules of the game.

---

##  Code Samples

###  1. Using a function
```python
def move(my_history, their_history):
    pick = random.choice(["r", "p", "s"])
    return pick
