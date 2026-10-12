# Number guessing game 

import random

number = random.randint(1, 10)

print("guess the number (1 to 10)")

while True:
    guess = int(input("your's guess"))
    if guess < number:
        print("very small number, try again")
    elif guess > number: 
        print("very big number, try again")
    else:
        print("very good! you guess the right number")