
import os
from dotenv import dotenv_values
from dotenv.main import load_dotenv

load_dotenv()


user = os.getenv("USER_NAME")


print(user)


#import random
from random import choice

print("...welcome to my game!")

x = input("Choose rock, paper, or scissors:")
print(x)
#if x == "rock": # "paper" "scissors"
#    print("VALID")
#else:
#    print("OOPS, INVALID, PLEASE TRY AGAIN")
#    exit()

if (x == "rock") or (x == "paper") or (x == "scissors"):
    print("VALID")
else:
    print("OOPS, INVALID, PLEASE TRY AGAIN")
    exit()
valid_options = ["rock", "paper", "scissors"]
#c = random.choice(valid_options)
c = choice(valid_options)
print("Computer Chose:", c)

if x == c:
    print("It's a tie. Try again!")
elif x == "rock" and c == "paper":
    print("Paper covers Rock. Sorry, you lose!")
elif x == "rock" and c == "scissors":
    print("Rock smashes scissors. Nice, you win!")
elif x == "paper" and c == "rock":
    print("Paper covers rock. Nice, you win!")
elif x == "paper" and c == "scissors":   
    print("Scissors cuts paper. Sorry, you lose!")
elif x == "scissors" and c == "rock":
    print("Rock smashes scissors. Sorry, you lose!")
elif x == "scissors" and c == "paper":
    print("Scissors cuts paper. Nice, you win!")
print(user)
print("...play again?")
