#Step 4
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.
lives = 6

print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display.extend("_")

#TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
# If lives goes down to 0 then the game should stop and it should print "You lose."
while "_" in display:
    guess = input("Guess a letter: ").lower()
    i = -1
    for letter in chosen_word:
        i += 1
        if guess == letter:
            display[i] = guess

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            break
    print(f"{' '.join(display)}")

if "_" not in display:
    print("You win!")
else:
    print("You lose!")
