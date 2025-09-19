# # guessing game.

import random
from random import randint

guessingNumber = 4
randomNumber = randint(1,5)

if guessingNumber == randomNumber: 
    print("You have won")
else: 
    print("You have lost")
    print("The random number was", randomNumber)