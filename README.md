# My First Python App

An example Python application for students to run to test their local development environment setups.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/prof-rossetti/my-first-python-app) under your own control, then "clone" or download your remote copy onto your local computer. Mine was forked and named "RP."

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd ~/Desktop/RP
```

Use Anaconda to create and activate a new virtual environment, perhaps called "my-game-env":

```sh
conda create -n my-first-env python=3.8
conda activate my-first-env
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above).

Once you have activated the environment, let's set the instructions for the game. 

Enter the code below for the welcome message:

'''py
print("Choose Rock, Paper, or Scissors:")

Run the game by typing the code below:

'''py
python game.py

If your message reads, you've successfully coded the first part of the game. If you get an error message, please check your code. 

Next, it's important to code the user's input:

'''py

x = input("Choose rock, paper, or scissors:")
print(x)

To ensure you're on the right track, run the game again and make a selection. If you choose anything other than the three choices in the parenthesis, your game should display an error message.

THe next step in the process is to ensure you can program the computer's choice. Please make sure to incorporate the code below for the randomization feature:

'''py
#import random
from random import choice

Once computer randomization is chosen, ensure winning and losing logic is programmed:

'''py
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

    Program a final message to the user to prompt another game:

'''py
print("...play again?")


## Setup

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username (then make sure to SAVE the ".env" file aftwards):

    USER_NAME="Alex"
    

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [".gitignore"](/.gitignore) file). This means we need to instruct each person who uses our code needs to create their own local ".env" file.

## Usage

Run the Python script:

```py
python app/my_script.py

# alternative module-style invocation (only required if importing from one file to another):
python -m app.my_script
```


> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment.


##References
Shout out to Professor Rossetti for the link to the README which was used as a foundation for these instructions. Great exercise!


