# 3-player Rock, Paper, Scissors: "Beat Geet" Edition 

# Who is this program for?
This is a fun and beginner-friendly game for people that are bored during the summer. It's made for students that want to a fun game to use, and also learn basic loops, lists, and functions. 

# What does the program do?
This program will randomly generate a move such as (rock, paper, or scissors) since it is a 3 player game you use your own funtion 'move()', then it decides who wins based of the rules of the game.


## Code examples 

### 1. Using a function
'''python
def move(my_move, their_move):
   pick = random.choice(["r", "p", "s"])
   return pick
