import random
from arts import *
from functions import *

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


