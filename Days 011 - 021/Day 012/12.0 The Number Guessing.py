#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from NumberGuessing_arts import *
from NumberGuessing_functions import *

random_number = random.randint(1, 100)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
#print(f"DEBUG: That number is {random_number}")

life_counter = game_difficulty()


while True:
    if life_counter == 0:
        print("\nYou've run out of guesses, you lose.")
        print(f"The correct number is {random_number}")
        break
    print(f"\nYou have {life_counter} attempts remaining to guess the number.")
    guess = input("Make a guess: ")
    try:
        guess = int(guess)
    except:
        print("Incorrect decision. Please repeat.")
        continue
    if guess == random_number:
        print(f"\nYou got it! The answer was {random_number}.")
        break
    elif guess > random_number:
        print("Too high.\nGuess again!")
        life_counter -= 1
    elif guess < random_number:
        print("Too low.\nGuess again!")
        life_counter -= 1
    else:
        print("Incorrect decision. Please repeat.\n")
        continue


