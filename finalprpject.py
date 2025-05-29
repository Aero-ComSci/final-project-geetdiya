import random 

strategy name = "Beat GeetnDiya" 

def move (my_history, their_history):
        pick = random.choice (["r", "p", "s"])
        if pick == "r":
            print("rock")
        if pick == "p":
            print("paper")
        if pick == "s":
            print("scissors")
        return pick

players = ["Player 1", "Player 2", "Player 3"]
moves= []

for names in players 
    print(player + "is playing:")
    m = move()
    moves.append(m)

print("n/Moves:")
print("Player 1:", moves = [0])
print("Player 2:", moves = [1])
print ("Player 3:", moves = [2])

if moves[0] == moves[1] == moves[2]:
    print("n/Result: Everyone Wins! Its a tie")
elif "r" in moves and "p" in moves and "s" in moves 
    print("n/Results: Its a tie! Everyone wins!")
else: 
print(n/Results: Two players picked the same choice, its a tie!")
