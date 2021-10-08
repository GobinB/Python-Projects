import random
from random import randint
from random import choice
board = [0]*25

ship = random.sample(list(range(24)), 5)
print(ship)
tries = 0  # tries
x = 0

for i in ship:
    board[i] = 1

while tries != 5:
    x = int(input("Guess where the ship Is:"))
    if board[x] == 1:
        tries = tries + 1
        print("Congratulations! You sunk the battleship")
        print("you sunk at : ", tries)

    elif board[x] == 0:
        tries = tries + 0
        print("it's a miss", tries)

    elif tries == 5:
        print("you won")


