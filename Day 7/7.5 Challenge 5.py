#Step 5

import random
import Challange5_words, Challange5_arts

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(Challange5_words.word_list)
lives = 6

display = []
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(Challange5_arts.logo)
for letter in chosen_word:
    display.extend("_")
while "_" in display:
    guess = input("Guess a letter: ").lower()
# TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"The letter '{guess}' has been already guessed. Try another one.")
    i = -1
    for letter in chosen_word:
        i += 1
        if guess == letter:
            display[i] = guess
    if guess not in chosen_word:
#TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"The letter '{guess}' is not in the chosen word.")
        lives -= 1
# TODO-2: - Import the stages from hangman_art.py and make this error go away.
        print(Challange5_arts.stages[lives])
        if lives == 0:
            break
    print(f"{' '.join(display)}")

if "_" not in display:
    print("You win!")
else:
    print(f"You lose! The chosen word is {chosen_word}")
