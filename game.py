from random import randint
print("Welcome to Rock-Paper-Scissors!")
moves = ["rock", "paper", "scissors"]
user_move = input("choose rock, paper, or scissors: ")
print(f"You chose: {user_move}")
print(f"Computer chose: {moves[randint(0, 2)]}")

