# Rock, Paper, scissor

import random

print("Rock, Paper, Scissor game")
print("write: rock, paper ya scissor")

user = input("your choice?: ").lower()
computer = random.choice(["rock", " paper", "scissor"])

if user != "rock" and user != "paper" and user != "scissor":
    print("wrong choice only rock, write paper or scissor")
else:
    print("choose by computer:, computer")

    if user == computer:
        print("Equal! Draw")
    elif user == "rock" and computer == "scissor":
        print("you win")
    elif user == "paper" and computer == "rock":
        print("you win")
    elif user == "scissor" and computer == "paper":
        print("you win")
    else:
        print("Computer win !")